const { contextBridge, ipcRenderer } = require('electron');
const path = require('path');

// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld('electronAPI', {
  // Git operations
  gitStatus: (repoPath) => ipcRenderer.invoke('git:status', repoPath),
  gitLog: (repoPath) => ipcRenderer.invoke('git:log', repoPath),
  gitBranches: (repoPath) => ipcRenderer.invoke('git:branches', repoPath),
  gitDiff: (repoPath, file) => ipcRenderer.invoke('git:diff', repoPath, file),
  gitCommit: (repoPath, message) => ipcRenderer.invoke('git:commit', repoPath, message),
  gitAdd: (repoPath, files) => ipcRenderer.invoke('git:add', repoPath, files),
  gitCheckout: (repoPath, branch) => ipcRenderer.invoke('git:checkout', repoPath, branch),
  gitPull: (repoPath) => ipcRenderer.invoke('git:pull', repoPath),
  gitPush: (repoPath) => ipcRenderer.invoke('git:push', repoPath),
  
  // AI operations
  aiSuggestCommit: (diff) => ipcRenderer.invoke('ai:suggest-commit', diff),
  
  // Dialog operations
  openDirectory: () => ipcRenderer.invoke('dialog:openDirectory'),
  
  // File system operations
  writeFile: (filePath, content) => ipcRenderer.invoke('fs:writeFile', filePath, content),
  exists: (filePath) => ipcRenderer.invoke('fs:exists', filePath),
  
  // Path utilities (safe to expose)
  pathJoin: (...args) => path.join(...args),
  pathDirname: (p) => path.dirname(p),
});
