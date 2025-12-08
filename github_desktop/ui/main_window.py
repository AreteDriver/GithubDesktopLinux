"""Main application window."""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSplitter,
    QPushButton, QLabel, QListWidget, QTextEdit, QLineEdit,
    QTabWidget, QStatusBar, QMenuBar, QMenu, QFileDialog,
    QMessageBox, QInputDialog, QListWidgetItem, QTreeWidget,
    QTreeWidgetItem
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QAction, QIcon
import os
from pathlib import Path

from github_desktop.core.github_client import GitHubClient
from github_desktop.core.git_operations import GitRepository
from github_desktop.utils.theme import Theme
from github_desktop.ui.auth_dialog import AuthDialog
from github_desktop.ui.commit_dialog import CommitDialog
from github_desktop.ui.clone_dialog import CloneDialog


class MainWindow(QMainWindow):
    """Main application window for GitHub Desktop."""
    
    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        
        self.github_client = GitHubClient()
        self.current_repo: GitRepository = None
        self.repos_path = str(Path.home() / "Documents" / "GitHub")
        
        # Ensure repos directory exists
        Path(self.repos_path).mkdir(parents=True, exist_ok=True)
        
        self.init_ui()
        self.apply_theme()
        
        # Try to load stored credentials
        if self.github_client.load_stored_token():
            self.on_authenticated()
        else:
            self.show_auth_dialog()
    
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("GitHub Desktop for Ubuntu")
        self.setGeometry(100, 100, 1200, 800)
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout(central_widget)
        
        # Create splitter for resizable panels
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Left panel - Repository list
        left_panel = self.create_left_panel()
        splitter.addWidget(left_panel)
        
        # Right panel - Repository details
        right_panel = self.create_right_panel()
        splitter.addWidget(right_panel)
        
        # Set splitter sizes
        splitter.setSizes([300, 900])
        
        main_layout.addWidget(splitter)
        
        # Create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
    
    def create_menu_bar(self):
        """Create the menu bar."""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("&File")
        
        clone_action = QAction("Clone Repository...", self)
        clone_action.setShortcut("Ctrl+Shift+O")
        clone_action.triggered.connect(self.clone_repository)
        file_menu.addAction(clone_action)
        
        add_local_action = QAction("Add Local Repository...", self)
        add_local_action.setShortcut("Ctrl+O")
        add_local_action.triggered.connect(self.add_local_repository)
        file_menu.addAction(add_local_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Repository menu
        repo_menu = menubar.addMenu("&Repository")
        
        fetch_action = QAction("Fetch", self)
        fetch_action.setShortcut("Ctrl+Shift+F")
        fetch_action.triggered.connect(self.fetch_repository)
        repo_menu.addAction(fetch_action)
        
        pull_action = QAction("Pull", self)
        pull_action.setShortcut("Ctrl+Shift+P")
        pull_action.triggered.connect(self.pull_repository)
        repo_menu.addAction(pull_action)
        
        push_action = QAction("Push", self)
        push_action.setShortcut("Ctrl+P")
        push_action.triggered.connect(self.push_repository)
        repo_menu.addAction(push_action)
        
        repo_menu.addSeparator()
        
        view_on_github = QAction("View on GitHub", self)
        view_on_github.setShortcut("Ctrl+Shift+G")
        view_on_github.triggered.connect(self.view_on_github)
        repo_menu.addAction(view_on_github)
        
        # Branch menu
        branch_menu = menubar.addMenu("&Branch")
        
        new_branch_action = QAction("New Branch...", self)
        new_branch_action.setShortcut("Ctrl+Shift+N")
        new_branch_action.triggered.connect(self.create_branch)
        branch_menu.addAction(new_branch_action)
        
        switch_branch_action = QAction("Switch Branch...", self)
        switch_branch_action.setShortcut("Ctrl+B")
        switch_branch_action.triggered.connect(self.switch_branch)
        branch_menu.addAction(switch_branch_action)
        
        # Help menu
        help_menu = menubar.addMenu("&Help")
        
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def create_left_panel(self):
        """Create the left panel with repository list."""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Header
        header_layout = QHBoxLayout()
        header_label = QLabel("<h3>Repositories</h3>")
        header_layout.addWidget(header_label)
        header_layout.addStretch()
        
        refresh_btn = QPushButton("↻")
        refresh_btn.setMaximumWidth(40)
        refresh_btn.clicked.connect(self.refresh_repositories)
        header_layout.addWidget(refresh_btn)
        
        layout.addLayout(header_layout)
        
        # Repository list
        self.repo_list = QListWidget()
        self.repo_list.itemClicked.connect(self.on_repo_selected)
        layout.addWidget(self.repo_list)
        
        # Action buttons
        btn_layout = QHBoxLayout()
        
        clone_btn = QPushButton("Clone")
        clone_btn.clicked.connect(self.clone_repository)
        btn_layout.addWidget(clone_btn)
        
        add_btn = QPushButton("Add")
        add_btn.clicked.connect(self.add_local_repository)
        btn_layout.addWidget(add_btn)
        
        layout.addLayout(btn_layout)
        
        return panel
    
    def create_right_panel(self):
        """Create the right panel with repository details."""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Repository header
        self.repo_header = QLabel("<h2>Select a repository</h2>")
        layout.addWidget(self.repo_header)
        
        # Current branch display
        branch_layout = QHBoxLayout()
        self.branch_label = QLabel("Branch: ")
        branch_layout.addWidget(self.branch_label)
        branch_layout.addStretch()
        
        self.branch_btn = QPushButton("Switch Branch")
        self.branch_btn.clicked.connect(self.switch_branch)
        self.branch_btn.setEnabled(False)
        branch_layout.addWidget(self.branch_btn)
        
        layout.addLayout(branch_layout)
        
        # Tabs for different views
        self.tab_widget = QTabWidget()
        
        # Changes tab
        changes_tab = self.create_changes_tab()
        self.tab_widget.addTab(changes_tab, "Changes")
        
        # History tab
        history_tab = self.create_history_tab()
        self.tab_widget.addTab(history_tab, "History")
        
        layout.addWidget(self.tab_widget)
        
        # Action buttons
        action_layout = QHBoxLayout()
        action_layout.addStretch()
        
        self.fetch_btn = QPushButton("Fetch")
        self.fetch_btn.clicked.connect(self.fetch_repository)
        self.fetch_btn.setEnabled(False)
        action_layout.addWidget(self.fetch_btn)
        
        self.pull_btn = QPushButton("Pull")
        self.pull_btn.clicked.connect(self.pull_repository)
        self.pull_btn.setEnabled(False)
        action_layout.addWidget(self.pull_btn)
        
        self.push_btn = QPushButton("Push")
        self.push_btn.clicked.connect(self.push_repository)
        self.push_btn.setEnabled(False)
        action_layout.addWidget(self.push_btn)
        
        layout.addLayout(action_layout)
        
        return panel
    
    def create_changes_tab(self):
        """Create the changes tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Changed files list
        files_label = QLabel("<b>Changed Files</b>")
        layout.addWidget(files_label)
        
        self.changed_files_list = QListWidget()
        self.changed_files_list.itemClicked.connect(self.on_file_selected)
        layout.addWidget(self.changed_files_list)
        
        # Diff view
        diff_label = QLabel("<b>Diff</b>")
        layout.addWidget(diff_label)
        
        self.diff_view = QTextEdit()
        self.diff_view.setReadOnly(True)
        self.diff_view.setFontFamily("monospace")
        layout.addWidget(self.diff_view)
        
        # Commit section
        commit_label = QLabel("<b>Commit Changes</b>")
        layout.addWidget(commit_label)
        
        self.commit_message = QTextEdit()
        self.commit_message.setPlaceholderText("Summary (required)")
        self.commit_message.setMaximumHeight(100)
        layout.addWidget(self.commit_message)
        
        commit_btn = QPushButton("Commit to current branch")
        commit_btn.clicked.connect(self.commit_changes)
        layout.addWidget(commit_btn)
        
        return widget
    
    def create_history_tab(self):
        """Create the history tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        history_label = QLabel("<b>Commit History</b>")
        layout.addWidget(history_label)
        
        self.history_list = QListWidget()
        self.history_list.itemClicked.connect(self.on_commit_selected)
        layout.addWidget(self.history_list)
        
        # Commit details
        details_label = QLabel("<b>Commit Details</b>")
        layout.addWidget(details_label)
        
        self.commit_details = QTextEdit()
        self.commit_details.setReadOnly(True)
        self.commit_details.setFontFamily("monospace")
        layout.addWidget(self.commit_details)
        
        return widget
    
    def apply_theme(self):
        """Apply application theme."""
        self.setStyleSheet(Theme.get_stylesheet())
    
    def show_auth_dialog(self):
        """Show authentication dialog."""
        dialog = AuthDialog(self)
        if dialog.exec():
            token = dialog.get_token()
            if self.github_client.authenticate(token):
                self.on_authenticated()
            else:
                QMessageBox.critical(
                    self,
                    "Authentication Failed",
                    "Failed to authenticate with GitHub. Please check your token."
                )
                self.show_auth_dialog()
    
    def on_authenticated(self):
        """Handle successful authentication."""
        user = self.github_client.get_user()
        if user:
            self.status_bar.showMessage(f"Logged in as {user.login}")
            self.refresh_repositories()
    
    def refresh_repositories(self):
        """Refresh the repository list."""
        self.repo_list.clear()
        
        # Add local repositories
        repos_path = Path(self.repos_path)
        if repos_path.exists():
            for item in repos_path.iterdir():
                if item.is_dir() and (item / ".git").exists():
                    item_widget = QListWidgetItem(f"📁 {item.name}")
                    item_widget.setData(Qt.ItemDataRole.UserRole, str(item))
                    self.repo_list.addItem(item_widget)
        
        self.status_bar.showMessage("Repositories refreshed")
    
    def on_repo_selected(self, item: QListWidgetItem):
        """Handle repository selection."""
        repo_path = item.data(Qt.ItemDataRole.UserRole)
        self.current_repo = GitRepository(repo_path)
        
        if self.current_repo.is_valid:
            self.repo_header.setText(f"<h2>{Path(repo_path).name}</h2>")
            self.update_repo_info()
            self.load_changed_files()
            self.load_commit_history()
            
            # Enable buttons
            self.branch_btn.setEnabled(True)
            self.fetch_btn.setEnabled(True)
            self.pull_btn.setEnabled(True)
            self.push_btn.setEnabled(True)
    
    def update_repo_info(self):
        """Update repository information display."""
        if not self.current_repo:
            return
        
        branch = self.current_repo.get_current_branch()
        if branch:
            self.branch_label.setText(f"Branch: <b>{branch}</b>")
        else:
            self.branch_label.setText("Branch: <i>No branch</i>")
    
    def load_changed_files(self):
        """Load changed files for current repository."""
        self.changed_files_list.clear()
        
        if not self.current_repo:
            return
        
        modified = self.current_repo.get_modified_files()
        for file in modified:
            self.changed_files_list.addItem(file)
        
        if modified:
            self.diff_view.setText(self.current_repo.get_diff() or "No diff available")
        else:
            self.diff_view.setText("No changes")
    
    def load_commit_history(self):
        """Load commit history for current repository."""
        self.history_list.clear()
        
        if not self.current_repo:
            return
        
        commits = self.current_repo.get_commit_history()
        for commit in commits:
            item_text = f"{commit['short_sha']} - {commit['message'][:50]}... by {commit['author']}"
            item = QListWidgetItem(item_text)
            item.setData(Qt.ItemDataRole.UserRole, commit)
            self.history_list.addItem(item)
    
    def on_file_selected(self, item: QListWidgetItem):
        """Handle file selection in changes list."""
        if not self.current_repo:
            return
        
        # Show diff for this file (simplified for now)
        self.diff_view.setText(self.current_repo.get_diff() or "No diff available")
    
    def on_commit_selected(self, item: QListWidgetItem):
        """Handle commit selection in history list."""
        commit = item.data(Qt.ItemDataRole.UserRole)
        if not commit or not self.current_repo:
            return
        
        details = f"""Commit: {commit['sha']}
Author: {commit['author']} <{commit['email']}>
Date: {commit['timestamp']}

{commit['message']}

---

{self.current_repo.get_diff(commit['sha']) or 'No diff available'}
"""
        self.commit_details.setText(details)
    
    def clone_repository(self):
        """Show clone repository dialog."""
        dialog = CloneDialog(self, self.github_client)
        if dialog.exec():
            url, path = dialog.get_clone_info()
            if url and path:
                self.status_bar.showMessage(f"Cloning {url}...")
                repo = GitRepository.clone(url, path)
                if repo:
                    self.status_bar.showMessage("Clone successful")
                    self.refresh_repositories()
                else:
                    QMessageBox.critical(self, "Error", "Failed to clone repository")
                    self.status_bar.showMessage("Clone failed")
    
    def add_local_repository(self):
        """Add an existing local repository."""
        path = QFileDialog.getExistingDirectory(
            self,
            "Select Repository Directory",
            str(Path.home())
        )
        
        if path:
            repo = GitRepository(path)
            if repo.is_valid:
                self.refresh_repositories()
                self.status_bar.showMessage(f"Added repository: {Path(path).name}")
            else:
                QMessageBox.warning(
                    self,
                    "Invalid Repository",
                    "The selected directory is not a valid Git repository."
                )
    
    def commit_changes(self):
        """Commit changes to the repository."""
        if not self.current_repo:
            return
        
        message = self.commit_message.toPlainText().strip()
        if not message:
            QMessageBox.warning(self, "Error", "Please enter a commit message")
            return
        
        # Get user info from git config
        user_name, user_email = self.current_repo.get_user_info()
        
        # Stage all changes
        if self.current_repo.stage_all():
            commit_sha = self.current_repo.commit(message, user_name, user_email)
            if commit_sha:
                self.status_bar.showMessage(f"Committed: {commit_sha[:7]}")
                self.commit_message.clear()
                self.load_changed_files()
                self.load_commit_history()
            else:
                QMessageBox.critical(self, "Error", "Failed to create commit")
        else:
            QMessageBox.critical(self, "Error", "Failed to stage changes")
    
    def fetch_repository(self):
        """Fetch changes from remote."""
        if not self.current_repo:
            return
        
        self.status_bar.showMessage("Fetching...")
        # Fetch implementation would go here
        QMessageBox.information(self, "Info", "Fetch functionality coming soon")
    
    def pull_repository(self):
        """Pull changes from remote."""
        if not self.current_repo:
            return
        
        self.status_bar.showMessage("Pulling...")
        success, message = self.current_repo.pull()
        
        if success:
            self.status_bar.showMessage("Pull successful")
            self.load_changed_files()
            self.load_commit_history()
        else:
            QMessageBox.critical(self, "Pull Failed", message)
            self.status_bar.showMessage("Pull failed")
    
    def push_repository(self):
        """Push changes to remote."""
        if not self.current_repo:
            return
        
        self.status_bar.showMessage("Pushing...")
        success, message = self.current_repo.push()
        
        if success:
            self.status_bar.showMessage("Push successful")
        else:
            QMessageBox.critical(self, "Push Failed", message)
            self.status_bar.showMessage("Push failed")
    
    def create_branch(self):
        """Create a new branch."""
        if not self.current_repo:
            return
        
        branch_name, ok = QInputDialog.getText(
            self,
            "Create Branch",
            "Enter branch name:"
        )
        
        if ok and branch_name:
            if self.current_repo.create_branch(branch_name):
                self.status_bar.showMessage(f"Created branch: {branch_name}")
                self.update_repo_info()
            else:
                QMessageBox.critical(self, "Error", "Failed to create branch")
    
    def switch_branch(self):
        """Switch to a different branch."""
        if not self.current_repo:
            return
        
        branches = self.current_repo.get_branches()
        if not branches:
            QMessageBox.information(self, "Info", "No branches available")
            return
        
        branch, ok = QInputDialog.getItem(
            self,
            "Switch Branch",
            "Select branch:",
            branches,
            0,
            False
        )
        
        if ok and branch:
            if self.current_repo.checkout_branch(branch):
                self.status_bar.showMessage(f"Switched to branch: {branch}")
                self.update_repo_info()
                self.load_changed_files()
                self.load_commit_history()
            else:
                QMessageBox.critical(self, "Error", "Failed to switch branch")
    
    def view_on_github(self):
        """Open current repository on GitHub."""
        if not self.current_repo:
            return
        
        url = self.current_repo.get_remote_url()
        if url:
            import webbrowser
            # Convert git URL to https
            if url.startswith("git@github.com:"):
                url = url.replace("git@github.com:", "https://github.com/")
            if url.endswith(".git"):
                url = url[:-4]
            webbrowser.open(url)
        else:
            QMessageBox.information(self, "Info", "No remote URL configured")
    
    def show_about(self):
        """Show about dialog."""
        QMessageBox.about(
            self,
            "About GitHub Desktop for Ubuntu",
            """<h2>GitHub Desktop for Ubuntu</h2>
            <p>Version 1.0.0</p>
            <p>The best possible version of GitHub for Ubuntu desktop.</p>
            <p>Features:</p>
            <ul>
            <li>Modern, intuitive UI</li>
            <li>Full GitHub integration</li>
            <li>Advanced Git operations</li>
            <li>Pull request management</li>
            <li>Syntax highlighted diffs</li>
            <li>Dark/Light theme support</li>
            </ul>
            """
        )
