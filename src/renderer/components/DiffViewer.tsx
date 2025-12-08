import React from 'react';

interface DiffViewerProps {
  diff: string;
}

export const DiffViewer: React.FC<DiffViewerProps> = ({ diff }) => {
  const renderDiff = () => {
    if (!diff) {
      return <div style={{ color: '#858585' }}>No changes to display</div>;
    }

    const lines = diff.split('\n');
    return lines.map((line, index) => {
      let className = 'diff-line context';
      
      if (line.startsWith('+') && !line.startsWith('+++')) {
        className = 'diff-line addition';
      } else if (line.startsWith('-') && !line.startsWith('---')) {
        className = 'diff-line deletion';
      } else if (line.startsWith('@@')) {
        className = 'diff-line context';
      }

      return (
        <div key={index} className={className}>
          {line || ' '}
        </div>
      );
    });
  };

  return <div className="diff-viewer">{renderDiff()}</div>;
};
