import React from 'react';
import { GitLog } from '../utils/gitApi';

interface BranchVisualizationProps {
  log: GitLog | null;
}

export const BranchVisualization: React.FC<BranchVisualizationProps> = ({ log }) => {
  if (!log || !log.all || log.all.length === 0) {
    return (
      <div className="branch-graph">
        <div style={{ color: '#858585', textAlign: 'center' }}>No commit history available</div>
      </div>
    );
  }

  return (
    <div className="branch-graph">
      <h3 style={{ marginBottom: '20px', fontSize: '16px', color: '#ffffff' }}>
        Commit History
      </h3>
      {log.all.map((commit, index) => (
        <div key={commit.hash} className="commit-node">
          <div className="commit-dot"></div>
          {index < log.all.length - 1 && <div className="commit-line"></div>}
          <div className="commit-info">
            <div className="commit-message">{commit.message}</div>
            <div className="commit-meta">
              <span className="commit-hash">{commit.hash.substring(0, 7)}</span>
              <span>{commit.author_name}</span>
              <span style={{ marginLeft: '10px' }}>
                {new Date(commit.date).toLocaleDateString()}
              </span>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};
