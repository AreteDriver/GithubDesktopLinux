const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const path = require('path');
const simpleGit = require('simple-git');
const fs = require('fs');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1280,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
    icon: path.join(__dirname, '../../assets/icon.png'),
    backgroundColor: '#1e1e1e',
  });

  // Load the app
  if (process.env.NODE_ENV === 'development') {
    mainWindow.loadFile(path.join(__dirname, '../../dist/index.html'));
    mainWindow.webContents.openDevTools();
  } else {
    mainWindow.loadFile(path.join(__dirname, '../../dist/index.html'));
  }

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});

// IPC handlers for Git operations
ipcMain.handle('git:status', async (event, repoPath) => {
  try {
    const git = simpleGit(repoPath);
    const status = await git.status();
    return { success: true, data: status };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

ipcMain.handle('git:log', async (event, repoPath) => {
  try {
    const git = simpleGit(repoPath);
    const log = await git.log({ maxCount: 100 });
    return { success: true, data: log };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

ipcMain.handle('git:branches', async (event, repoPath) => {
  try {
    const git = simpleGit(repoPath);
    const branches = await git.branch();
    return { success: true, data: branches };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

ipcMain.handle('git:diff', async (event, repoPath, file) => {
  try {
    const git = simpleGit(repoPath);
    const diff = file 
      ? await git.diff(['--', file])
      : await git.diff();
    return { success: true, data: diff };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

ipcMain.handle('git:commit', async (event, repoPath, message) => {
  try {
    const git = simpleGit(repoPath);
    await git.commit(message);
    return { success: true };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

ipcMain.handle('git:add', async (event, repoPath, files) => {
  try {
    const git = simpleGit(repoPath);
    await git.add(files);
    return { success: true };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

ipcMain.handle('git:checkout', async (event, repoPath, branch) => {
  try {
    const git = simpleGit(repoPath);
    await git.checkout(branch);
    return { success: true };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

ipcMain.handle('git:pull', async (event, repoPath) => {
  try {
    const git = simpleGit(repoPath);
    await git.pull();
    return { success: true };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

ipcMain.handle('git:push', async (event, repoPath) => {
  try {
    const git = simpleGit(repoPath);
    await git.push();
    return { success: true };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

// AI-powered commit message suggestion
ipcMain.handle('ai:suggest-commit', async (event, diff) => {
  try {
    // Simple rule-based commit message generation
    // In a production app, this would integrate with an AI service
    const suggestions = generateCommitMessage(diff);
    return { success: true, data: suggestions };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

function generateCommitMessage(diff) {
  // Simple heuristic-based commit message generation
  const lines = diff.split('\n');
  const additions = lines.filter(l => l.startsWith('+')).length;
  const deletions = lines.filter(l => l.startsWith('-')).length;
  
  const suggestions = [];
  
  if (additions > deletions * 2) {
    suggestions.push('feat: Add new functionality');
    suggestions.push('feature: Implement new feature');
  } else if (deletions > additions * 2) {
    suggestions.push('refactor: Remove unused code');
    suggestions.push('cleanup: Remove deprecated functionality');
  } else {
    suggestions.push('fix: Update implementation');
    suggestions.push('chore: Update codebase');
  }
  
  // Check for specific patterns
  if (diff.includes('test') || diff.includes('spec')) {
    suggestions.unshift('test: Update tests');
  }
  if (diff.includes('README') || diff.includes('docs')) {
    suggestions.unshift('docs: Update documentation');
  }
  if (diff.includes('package.json')) {
    suggestions.unshift('chore: Update dependencies');
  }
  
  return suggestions.slice(0, 3);
}

// Dialog handlers
ipcMain.handle('dialog:openDirectory', async () => {
  const result = await dialog.showOpenDialog(mainWindow, {
    properties: ['openDirectory'],
  });
  return result;
});

// File system handlers
ipcMain.handle('fs:writeFile', async (event, filePath, content) => {
  try {
    const dir = path.dirname(filePath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
    fs.writeFileSync(filePath, content);
    return { success: true };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

ipcMain.handle('fs:exists', async (event, filePath) => {
  try {
    return { success: true, exists: fs.existsSync(filePath) };
  } catch (error) {
    return { success: false, error: error.message };
  }
});
