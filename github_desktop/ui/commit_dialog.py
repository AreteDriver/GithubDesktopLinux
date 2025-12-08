"""Commit dialog for creating commits."""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit,
    QPushButton, QListWidget
)
from PyQt6.QtCore import Qt


class CommitDialog(QDialog):
    """Dialog for creating commits."""
    
    def __init__(self, parent=None, changed_files=None):
        """Initialize the commit dialog."""
        super().__init__(parent)
        
        self.changed_files = changed_files or []
        self.commit_message = None
        
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Commit Changes")
        self.setModal(True)
        self.setMinimumWidth(500)
        self.setMinimumHeight(400)
        
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("<h2>Commit Changes</h2>")
        layout.addWidget(title)
        
        # Changed files
        files_label = QLabel(f"<b>Changed Files ({len(self.changed_files)}):</b>")
        layout.addWidget(files_label)
        
        self.files_list = QListWidget()
        for file in self.changed_files:
            self.files_list.addItem(file)
        layout.addWidget(self.files_list)
        
        # Commit message
        message_label = QLabel("<b>Commit Message:</b>")
        layout.addWidget(message_label)
        
        self.summary_input = QTextEdit()
        self.summary_input.setPlaceholderText("Summary (required)")
        self.summary_input.setMaximumHeight(60)
        layout.addWidget(self.summary_input)
        
        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("Description (optional)")
        layout.addWidget(self.description_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        commit_btn = QPushButton("Commit")
        commit_btn.setDefault(True)
        commit_btn.clicked.connect(self.accept)
        button_layout.addWidget(commit_btn)
        
        layout.addLayout(button_layout)
    
    def get_commit_message(self) -> str:
        """Get the complete commit message."""
        summary = self.summary_input.toPlainText().strip()
        description = self.description_input.toPlainText().strip()
        
        if description:
            return f"{summary}\n\n{description}"
        return summary
