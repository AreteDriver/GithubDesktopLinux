import React, { useState } from 'react';
import { getAllTemplates, RepoTemplate } from '../utils/templates';

interface TemplateModalProps {
  onClose: () => void;
  onSelect: (template: RepoTemplate) => void;
}

export const TemplateModal: React.FC<TemplateModalProps> = ({ onClose, onSelect }) => {
  const templates = getAllTemplates();

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <h2>Choose a Repository Template</h2>
        <p style={{ color: '#858585', marginBottom: '20px' }}>
          Select a template to initialize your repository with pre-configured files
        </p>
        <div className="template-grid">
          {templates.map((template) => (
            <div
              key={template.id}
              className="template-card"
              onClick={() => onSelect(template)}
            >
              <h3>{template.name}</h3>
              <p>{template.description}</p>
            </div>
          ))}
        </div>
        <div className="modal-actions">
          <button className="btn btn-secondary" onClick={onClose}>
            Cancel
          </button>
        </div>
      </div>
    </div>
  );
};
