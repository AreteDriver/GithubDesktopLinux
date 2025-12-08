"""Authentication dialog for GitHub login."""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QTextEdit
)
from PyQt6.QtCore import Qt


class AuthDialog(QDialog):
    """Dialog for GitHub authentication."""
    
    def __init__(self, parent=None):
        """Initialize the authentication dialog."""
        super().__init__(parent)
        
        self.token = None
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("GitHub Authentication")
        self.setModal(True)
        self.setMinimumWidth(500)
        
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("<h2>Sign in to GitHub</h2>")
        layout.addWidget(title)
        
        # Instructions
        instructions = QTextEdit()
        instructions.setReadOnly(True)
        instructions.setMaximumHeight(120)
        instructions.setHtml("""
            <p>To use GitHub Desktop, you need a Personal Access Token.</p>
            <ol>
                <li>Go to <a href="https://github.com/settings/tokens">GitHub Settings → Developer settings → Personal access tokens</a></li>
                <li>Click "Generate new token (classic)"</li>
                <li>Select scopes: <b>repo</b>, <b>user</b>, <b>workflow</b></li>
                <li>Copy the generated token and paste it below</li>
            </ol>
        """)
        instructions.setOpenExternalLinks(True)
        layout.addWidget(instructions)
        
        # Token input
        token_label = QLabel("Personal Access Token:")
        layout.addWidget(token_label)
        
        self.token_input = QLineEdit()
        self.token_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.token_input.setPlaceholderText("ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        layout.addWidget(self.token_input)
        
        # Show/Hide token checkbox
        show_token_layout = QHBoxLayout()
        self.show_token_btn = QPushButton("Show Token")
        self.show_token_btn.setCheckable(True)
        self.show_token_btn.toggled.connect(self.toggle_token_visibility)
        show_token_layout.addWidget(self.show_token_btn)
        show_token_layout.addStretch()
        layout.addLayout(show_token_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        login_btn = QPushButton("Sign In")
        login_btn.setDefault(True)
        login_btn.clicked.connect(self.accept)
        button_layout.addWidget(login_btn)
        
        layout.addLayout(button_layout)
    
    def toggle_token_visibility(self, checked):
        """Toggle token visibility."""
        if checked:
            self.token_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.show_token_btn.setText("Hide Token")
        else:
            self.token_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.show_token_btn.setText("Show Token")
    
    def get_token(self) -> str:
        """Get the entered token."""
        return self.token_input.text().strip()
