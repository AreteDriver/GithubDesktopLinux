const { ipcRenderer } = window.require('electron');

export interface GitStatus {
  current: string;
  tracking: string | null;
  ahead: number;
  behind: number;
  files: Array<{
    path: string;
    index: string;
    working_dir: string;
  }>;
}

export interface GitLog {
  all: Array<{
    hash: string;
    date: string;
    message: string;
    author_name: string;
    author_email: string;
  }>;
}

export interface GitBranches {
  current: string;
  all: string[];
  branches: { [key: string]: { current: boolean; name: string; commit: string; label: string } };
}

export const gitApi = {
  status: (repoPath: string): Promise<{ success: boolean; data?: GitStatus; error?: string }> => {
    return ipcRenderer.invoke('git:status', repoPath);
  },

  log: (repoPath: string): Promise<{ success: boolean; data?: GitLog; error?: string }> => {
    return ipcRenderer.invoke('git:log', repoPath);
  },

  branches: (repoPath: string): Promise<{ success: boolean; data?: GitBranches; error?: string }> => {
    return ipcRenderer.invoke('git:branches', repoPath);
  },

  diff: (repoPath: string, file?: string): Promise<{ success: boolean; data?: string; error?: string }> => {
    return ipcRenderer.invoke('git:diff', repoPath, file);
  },

  commit: (repoPath: string, message: string): Promise<{ success: boolean; error?: string }> => {
    return ipcRenderer.invoke('git:commit', repoPath, message);
  },

  add: (repoPath: string, files: string[]): Promise<{ success: boolean; error?: string }> => {
    return ipcRenderer.invoke('git:add', repoPath, files);
  },

  checkout: (repoPath: string, branch: string): Promise<{ success: boolean; error?: string }> => {
    return ipcRenderer.invoke('git:checkout', repoPath, branch);
  },

  pull: (repoPath: string): Promise<{ success: boolean; error?: string }> => {
    return ipcRenderer.invoke('git:pull', repoPath);
  },

  push: (repoPath: string): Promise<{ success: boolean; error?: string }> => {
    return ipcRenderer.invoke('git:push', repoPath);
  },

  suggestCommitMessage: (diff: string): Promise<{ success: boolean; data?: string[]; error?: string }> => {
    return ipcRenderer.invoke('ai:suggest-commit', diff);
  },

  // Dialog API
  openDirectory: (): Promise<{ canceled: boolean; filePaths: string[] }> => {
    return ipcRenderer.invoke('dialog:openDirectory');
  },

  // File system API
  writeFile: (filePath: string, content: string): Promise<{ success: boolean; error?: string }> => {
    return ipcRenderer.invoke('fs:writeFile', filePath, content);
  },

  exists: (filePath: string): Promise<{ success: boolean; exists?: boolean; error?: string }> => {
    return ipcRenderer.invoke('fs:exists', filePath);
  },
};
