import React, { useState, useEffect } from 'react';
import { gitApi, GitStatus, GitBranches, GitLog } from './utils/gitApi';
import { DiffViewer } from './components/DiffViewer';
import { BranchVisualization } from './components/BranchVisualization';
import { CommitForm } from './components/CommitForm';
import { TemplateModal } from './components/TemplateModal';
import { RepoTemplate } from './utils/templates';
import './styles/App.css';

interface Notification {
  id: number;
  message: string;
  type: 'success' | 'error' | 'info';
}

function App() {
  const [repoPath, setRepoPath] = useState<string>('');
  const [status, setStatus] = useState<GitStatus | null>(null);
  const [branches, setBranches] = useState<GitBranches | null>(null);
  const [log, setLog] = useState<GitLog | null>(null);
  const [selectedFile, setSelectedFile] = useState<string | null>(null);
  const [diff, setDiff] = useState<string>('');
  const [activeTab, setActiveTab] = useState<'changes' | 'history' | 'branches'>('changes');
  const [error, setError] = useState<string>('');
  const [stagedFiles, setStagedFiles] = useState<string[]>([]);
  const [showTemplateModal, setShowTemplateModal] = useState(false);
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [notificationId, setNotificationId] = useState(0);

  const showNotification = (message: string, type: 'success' | 'error' | 'info' = 'info') => {
    const id = notificationId;
    setNotificationId(id + 1);
    setNotifications([...notifications, { id, message, type }]);
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
      setNotifications(prev => prev.filter(n => n.id !== id));
    }, 5000);
  };

  useEffect(() => {
    if (repoPath) {
      loadRepoData();
    }
  }, [repoPath]);

  const loadRepoData = async () => {
    try {
      setError('');
      const [statusResult, branchResult, logResult] = await Promise.all([
        gitApi.status(repoPath),
        gitApi.branches(repoPath),
        gitApi.log(repoPath),
      ]);

      if (statusResult.success && statusResult.data) {
        setStatus(statusResult.data);
      }
      if (branchResult.success && branchResult.data) {
        setBranches(branchResult.data);
      }
      if (logResult.success && logResult.data) {
        setLog(logResult.data);
      }
    } catch (err) {
      setError('Failed to load repository data');
      console.error(err);
    }
  };

  const handleOpenRepo = async () => {
    try {
      const result = await gitApi.openDirectory();

      if (!result.canceled && result.filePaths.length > 0) {
        setRepoPath(result.filePaths[0]);
      }
    } catch (err) {
      setError('Failed to open repository');
      console.error(err);
    }
  };

  const handleFileClick = async (file: string) => {
    setSelectedFile(file);
    const diffResult = await gitApi.diff(repoPath, file);
    if (diffResult.success && diffResult.data) {
      setDiff(diffResult.data);
    }
  };

  const handleStageFile = async (file: string) => {
    const result = await gitApi.add(repoPath, [file]);
    if (result.success) {
      setStagedFiles([...stagedFiles, file]);
      loadRepoData();
    }
  };

  const handleBranchSwitch = async (branch: string) => {
    const result = await gitApi.checkout(repoPath, branch);
    if (result.success) {
      loadRepoData();
      showNotification(`Switched to branch: ${branch}`, 'success');
    } else {
      showNotification(`Failed to switch branch: ${result.error}`, 'error');
    }
  };

  const handlePull = async () => {
    const result = await gitApi.pull(repoPath);
    if (result.success) {
      loadRepoData();
      showNotification('Pull successful', 'success');
    } else {
      showNotification(`Pull failed: ${result.error}`, 'error');
    }
  };

  const handlePush = async () => {
    const result = await gitApi.push(repoPath);
    if (result.success) {
      showNotification('Push successful', 'success');
    } else {
      showNotification(`Push failed: ${result.error}`, 'error');
    }
  };

  const handleCommitSuccess = () => {
    setStagedFiles([]);
    setSelectedFile(null);
    setDiff('');
    loadRepoData();
  };

  const handleTemplateSelect = async (template: RepoTemplate) => {
    try {
      // Create template files
      for (const [filePath, content] of Object.entries(template.files)) {
        const fullPath = gitApi.pathJoin(repoPath, filePath);
        const result = await gitApi.writeFile(fullPath, content);
        if (!result.success) {
          throw new Error(result.error);
        }
      }

      // Create .gitignore if specified
      if (template.gitignore) {
        const gitignorePath = gitApi.pathJoin(repoPath, '.gitignore');
        await gitApi.writeFile(gitignorePath, template.gitignore);
      }

      setShowTemplateModal(false);
      loadRepoData();
      showNotification(`Template "${template.name}" applied successfully!`, 'success');
    } catch (err) {
      showNotification(`Failed to apply template: ${err}`, 'error');
    }
  };

  const renderChangesTab = () => {
    if (!status) return null;

    const files = status.files || [];
    const unstagedFiles = files.filter(f => !stagedFiles.includes(f.path));

    return (
      <div>
        {error && <div className="error">{error}</div>}
        
        <CommitForm 
          repoPath={repoPath}
          stagedFiles={stagedFiles}
          onCommitSuccess={handleCommitSuccess}
          onNotification={showNotification}
        />

        <div style={{ marginBottom: '20px' }}>
          <h3 style={{ marginBottom: '15px', fontSize: '16px', color: '#ffffff' }}>
            Changed Files ({files.length})
          </h3>
          {files.length === 0 ? (
            <div style={{ color: '#858585', padding: '20px', textAlign: 'center' }}>
              No changes detected
            </div>
          ) : (
            <ul className="changes-list">
              {files.map((file) => {
                const isStaged = stagedFiles.includes(file.path);
                let statusLabel = 'M';
                let statusClass = 'modified';
                
                if (file.working_dir === 'D' || file.index === 'D') {
                  statusLabel = 'D';
                  statusClass = 'deleted';
                } else if (file.working_dir === '?' || file.index === 'A') {
                  statusLabel = 'A';
                  statusClass = 'added';
                }

                return (
                  <li 
                    key={file.path} 
                    className="change-item"
                    onClick={() => handleFileClick(file.path)}
                  >
                    <div className={`change-status ${statusClass}`}>
                      {statusLabel}
                    </div>
                    <div className="change-path">{file.path}</div>
                    {!isStaged && (
                      <button
                        className="btn btn-secondary"
                        onClick={(e) => {
                          e.stopPropagation();
                          handleStageFile(file.path);
                        }}
                        style={{ padding: '4px 12px', fontSize: '12px' }}
                      >
                        Stage
                      </button>
                    )}
                    {isStaged && (
                      <span style={{ color: '#2ea043', fontSize: '12px' }}>✓ Staged</span>
                    )}
                  </li>
                );
              })}
            </ul>
          )}
        </div>

        {selectedFile && (
          <div>
            <h3 style={{ marginBottom: '15px', fontSize: '16px', color: '#ffffff' }}>
              Diff: {selectedFile}
            </h3>
            <DiffViewer diff={diff} />
          </div>
        )}
      </div>
    );
  };

  const renderHistoryTab = () => {
    return <BranchVisualization log={log} />;
  };

  const renderBranchesTab = () => {
    if (!branches) return null;

    return (
      <div>
        <h3 style={{ marginBottom: '20px', fontSize: '16px', color: '#ffffff' }}>
          All Branches
        </h3>
        <ul className="changes-list">
          {branches.all.map((branch) => {
            const isCurrent = branch === branches.current;
            return (
              <li
                key={branch}
                className="change-item"
                style={{
                  backgroundColor: isCurrent ? '#094771' : 'transparent',
                }}
              >
                <span style={{ fontSize: '14px' }}>
                  {isCurrent ? '★ ' : ''}
                  {branch}
                </span>
                {!isCurrent && (
                  <button
                    className="btn btn-secondary"
                    onClick={() => handleBranchSwitch(branch)}
                    style={{ padding: '4px 12px', fontSize: '12px' }}
                  >
                    Switch
                  </button>
                )}
              </li>
            );
          })}
        </ul>
      </div>
    );
  };

  if (!repoPath) {
    return (
      <div className="app">
        <div className="welcome-screen">
          <h2>🚀 GitHub Desktop Linux</h2>
          <p>Modern Git client with AI-powered features</p>
          <div style={{ display: 'flex', gap: '15px' }}>
            <button className="btn" onClick={handleOpenRepo}>
              Open Repository
            </button>
            <button className="btn btn-secondary" onClick={() => setShowTemplateModal(true)}>
              View Templates
            </button>
          </div>
        </div>
        {showTemplateModal && (
          <TemplateModal
            onClose={() => setShowTemplateModal(false)}
            onSelect={handleTemplateSelect}
          />
        )}
      </div>
    );
  }

  return (
    <div className="app">
      <div className="sidebar">
        <div className="sidebar-header">
          <h1>GitHub Desktop Linux</h1>
          <div className="repo-path">{repoPath}</div>
        </div>

        <div className="sidebar-section">
          <h3>Current Branch</h3>
          <div style={{ padding: '10px', backgroundColor: '#094771', borderRadius: '4px' }}>
            {branches?.current || 'main'}
          </div>
        </div>

        <div className="sidebar-section">
          <h3>Quick Actions</h3>
          <button 
            className="btn" 
            style={{ width: '100%', marginBottom: '8px' }}
            onClick={handlePull}
          >
            Pull
          </button>
          <button 
            className="btn btn-secondary" 
            style={{ width: '100%', marginBottom: '8px' }}
            onClick={handlePush}
          >
            Push
          </button>
          <button 
            className="btn btn-secondary" 
            style={{ width: '100%' }}
            onClick={() => setShowTemplateModal(true)}
          >
            Apply Template
          </button>
        </div>
      </div>

      <div className="main-content">
        <div className="toolbar">
          <button className="btn btn-secondary" onClick={handleOpenRepo}>
            Change Repository
          </button>
          <button className="btn btn-secondary" onClick={loadRepoData}>
            Refresh
          </button>
        </div>

        <div className="tabs">
          <button
            className={`tab ${activeTab === 'changes' ? 'active' : ''}`}
            onClick={() => setActiveTab('changes')}
          >
            Changes
          </button>
          <button
            className={`tab ${activeTab === 'history' ? 'active' : ''}`}
            onClick={() => setActiveTab('history')}
          >
            History
          </button>
          <button
            className={`tab ${activeTab === 'branches' ? 'active' : ''}`}
            onClick={() => setActiveTab('branches')}
          >
            Branches
          </button>
        </div>

        <div className="content-area">
          {activeTab === 'changes' && renderChangesTab()}
          {activeTab === 'history' && renderHistoryTab()}
          {activeTab === 'branches' && renderBranchesTab()}
        </div>
      </div>

      {showTemplateModal && (
        <TemplateModal
          onClose={() => setShowTemplateModal(false)}
          onSelect={handleTemplateSelect}
        />
      )}

      {/* Notification System */}
      <div className="notifications">
        {notifications.map((notification) => (
          <div 
            key={notification.id} 
            className={`notification notification-${notification.type}`}
          >
            {notification.message}
            <button 
              className="notification-close"
              onClick={() => setNotifications(prev => prev.filter(n => n.id !== notification.id))}
            >
              ×
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
