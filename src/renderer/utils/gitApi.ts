// Access the exposed API from preload script
declare global {
  interface Window {
    electronAPI: {
      gitStatus: (repoPath: string) => Promise<{ success: boolean; data?: GitStatus; error?: string }>;
      gitLog: (repoPath: string) => Promise<{ success: boolean; data?: GitLog; error?: string }>;
      gitBranches: (repoPath: string) => Promise<{ success: boolean; data?: GitBranches; error?: string }>;
      gitDiff: (repoPath: string, file?: string) => Promise<{ success: boolean; data?: string; error?: string }>;
      gitCommit: (repoPath: string, message: string) => Promise<{ success: boolean; error?: string }>;
      gitAdd: (repoPath: string, files: string[]) => Promise<{ success: boolean; error?: string }>;
      gitCheckout: (repoPath: string, branch: string) => Promise<{ success: boolean; error?: string }>;
      gitPull: (repoPath: string) => Promise<{ success: boolean; error?: string }>;
      gitPush: (repoPath: string) => Promise<{ success: boolean; error?: string }>;
      aiSuggestCommit: (diff: string) => Promise<{ success: boolean; data?: string[]; error?: string }>;
      openDirectory: () => Promise<{ canceled: boolean; filePaths: string[] }>;
      writeFile: (filePath: string, content: string) => Promise<{ success: boolean; error?: string }>;
      exists: (filePath: string) => Promise<{ success: boolean; exists?: boolean; error?: string }>;
      pathJoin: (...args: string[]) => string;
      pathDirname: (path: string) => string;
    };
  }
}

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
  status: (repoPath: string) => window.electronAPI.gitStatus(repoPath),
  log: (repoPath: string) => window.electronAPI.gitLog(repoPath),
  branches: (repoPath: string) => window.electronAPI.gitBranches(repoPath),
  diff: (repoPath: string, file?: string) => window.electronAPI.gitDiff(repoPath, file),
  commit: (repoPath: string, message: string) => window.electronAPI.gitCommit(repoPath, message),
  add: (repoPath: string, files: string[]) => window.electronAPI.gitAdd(repoPath, files),
  checkout: (repoPath: string, branch: string) => window.electronAPI.gitCheckout(repoPath, branch),
  pull: (repoPath: string) => window.electronAPI.gitPull(repoPath),
  push: (repoPath: string) => window.electronAPI.gitPush(repoPath),
  suggestCommitMessage: (diff: string) => window.electronAPI.aiSuggestCommit(diff),
  openDirectory: () => window.electronAPI.openDirectory(),
  writeFile: (filePath: string, content: string) => window.electronAPI.writeFile(filePath, content),
  exists: (filePath: string) => window.electronAPI.exists(filePath),
  pathJoin: (...args: string[]) => window.electronAPI.pathJoin(...args),
  pathDirname: (path: string) => window.electronAPI.pathDirname(path),
};
