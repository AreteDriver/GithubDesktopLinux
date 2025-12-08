import React, { useState, useEffect } from 'react';
import { gitApi } from '../utils/gitApi';

interface CommitFormProps {
  repoPath: string;
  stagedFiles: string[];
  onCommitSuccess: () => void;
  onNotification: (message: string, type: 'success' | 'error' | 'info') => void;
}

export const CommitForm: React.FC<CommitFormProps> = ({ 
  repoPath, 
  stagedFiles, 
  onCommitSuccess,
  onNotification 
}) => {
  const [message, setMessage] = useState('');
  const [suggestions, setSuggestions] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [showSuggestions, setShowSuggestions] = useState(false);

  useEffect(() => {
    loadSuggestions();
  }, [stagedFiles]);

  const loadSuggestions = async () => {
    if (stagedFiles.length === 0) {
      setSuggestions([]);
      return;
    }

    try {
      const diffResult = await gitApi.diff(repoPath);
      if (diffResult.success && diffResult.data) {
        const suggestResult = await gitApi.suggestCommitMessage(diffResult.data);
        if (suggestResult.success && suggestResult.data) {
          setSuggestions(suggestResult.data);
          setShowSuggestions(true);
        }
      }
    } catch (error) {
      console.error('Failed to load suggestions:', error);
    }
  };

  const handleCommit = async () => {
    if (!message.trim() || stagedFiles.length === 0) {
      onNotification('Please enter a commit message and stage files', 'error');
      return;
    }

    setLoading(true);
    try {
      const result = await gitApi.commit(repoPath, message);
      if (result.success) {
        setMessage('');
        setSuggestions([]);
        setShowSuggestions(false);
        onNotification('Commit successful', 'success');
        onCommitSuccess();
      } else {
        onNotification(`Commit failed: ${result.error}`, 'error');
      }
    } catch (error) {
      onNotification(`Commit failed: ${error}`, 'error');
    } finally {
      setLoading(false);
    }
  };

  const applySuggestion = (suggestion: string) => {
    setMessage(suggestion);
    setShowSuggestions(false);
  };

  return (
    <div className="commit-form">
      <h3 style={{ marginBottom: '15px', fontSize: '16px', color: '#ffffff' }}>
        Commit Changes ({stagedFiles.length} file{stagedFiles.length !== 1 ? 's' : ''})
      </h3>
      <textarea
        className="commit-message"
        placeholder="Enter commit message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      {showSuggestions && suggestions.length > 0 && (
        <div className="ai-suggestions">
          <h4>✨ AI Suggestions</h4>
          <ul className="suggestion-list">
            {suggestions.map((suggestion, index) => (
              <li
                key={index}
                className="suggestion-item"
                onClick={() => applySuggestion(suggestion)}
              >
                {suggestion}
              </li>
            ))}
          </ul>
        </div>
      )}
      <div style={{ display: 'flex', gap: '10px', marginTop: '10px' }}>
        <button 
          className="btn" 
          onClick={handleCommit} 
          disabled={loading || !message.trim() || stagedFiles.length === 0}
        >
          {loading ? 'Committing...' : 'Commit'}
        </button>
        {!showSuggestions && suggestions.length > 0 && (
          <button 
            className="btn btn-secondary" 
            onClick={() => setShowSuggestions(true)}
          >
            Show AI Suggestions
          </button>
        )}
      </div>
    </div>
  );
};
