"""Clone repository dialog."""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QFileDialog, QComboBox, QListWidget
)
from PyQt6.QtCore import Qt
from pathlib import Path

from github_desktop.core.github_client import GitHubClient


class CloneDialog(QDialog):
    """Dialog for cloning repositories."""
    
    def __init__(self, parent=None, github_client: GitHubClient = None):
        """Initialize the clone dialog."""
        super().__init__(parent)
        
        self.github_client = github_client
        self.clone_url = None
        self.clone_path = None
        
        self.init_ui()
        
        if self.github_client and self.github_client.is_authenticated():
            self.load_repositories()
    
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Clone Repository")
        self.setModal(True)
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)
        
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("<h2>Clone a Repository</h2>")
        layout.addWidget(title)
        
        # Repository source tabs
        source_label = QLabel("<b>Repository URL or select from your repositories:</b>")
        layout.addWidget(source_label)
        
        # URL input
        url_layout = QHBoxLayout()
        url_label = QLabel("URL:")
        url_layout.addWidget(url_label)
        
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("https://github.com/user/repo.git")
        self.url_input.textChanged.connect(self.on_url_changed)
        url_layout.addWidget(self.url_input)
        
        layout.addLayout(url_layout)
        
        # Repository list
        repos_label = QLabel("Your repositories:")
        layout.addWidget(repos_label)
        
        self.repo_list = QListWidget()
        self.repo_list.itemClicked.connect(self.on_repo_selected)
        layout.addWidget(self.repo_list)
        
        # Local path
        path_label = QLabel("<b>Local Path:</b>")
        layout.addWidget(path_label)
        
        path_layout = QHBoxLayout()
        
        self.path_input = QLineEdit()
        default_path = str(Path.home() / "Documents" / "GitHub")
        self.path_input.setText(default_path)
        path_layout.addWidget(self.path_input)
        
        browse_btn = QPushButton("Browse...")
        browse_btn.clicked.connect(self.browse_path)
        path_layout.addWidget(browse_btn)
        
        layout.addLayout(path_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        clone_btn = QPushButton("Clone")
        clone_btn.setDefault(True)
        clone_btn.clicked.connect(self.accept)
        button_layout.addWidget(clone_btn)
        
        layout.addLayout(button_layout)
    
    def load_repositories(self):
        """Load user repositories from GitHub."""
        self.repo_list.clear()
        
        repos = self.github_client.get_user_repos()
        for repo in repos:
            self.repo_list.addItem(f"{repo.full_name} - {repo.description or 'No description'}")
            item = self.repo_list.item(self.repo_list.count() - 1)
            item.setData(Qt.ItemDataRole.UserRole, repo.clone_url)
    
    def on_repo_selected(self, item):
        """Handle repository selection."""
        clone_url = item.data(Qt.ItemDataRole.UserRole)
        self.url_input.setText(clone_url)
    
    def on_url_changed(self, text):
        """Handle URL input change."""
        # Extract repo name from URL for local path
        if text:
            parts = text.rstrip('/').split('/')
            if len(parts) > 0:
                repo_name = parts[-1].replace('.git', '')
                base_path = self.path_input.text()
                if '/Documents/GitHub' in base_path:
                    base_path = str(Path.home() / "Documents" / "GitHub")
                self.path_input.setText(str(Path(base_path) / repo_name))
    
    def browse_path(self):
        """Browse for local path."""
        path = QFileDialog.getExistingDirectory(
            self,
            "Select Directory",
            str(Path.home())
        )
        
        if path:
            self.path_input.setText(path)
    
    def get_clone_info(self):
        """Get clone URL and path."""
        return self.url_input.text().strip(), self.path_input.text().strip()
