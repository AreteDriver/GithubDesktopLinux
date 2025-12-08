# Developer Guide

This guide is for developers who want to understand, modify, or extend GitHub Desktop for Ubuntu.

## Architecture Overview

### High-Level Architecture

```
┌─────────────────────────────────────────┐
│          User Interface (UI)            │
│    PyQt6 Windows, Dialogs, Widgets      │
└────────────┬────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│       Application Layer (Core)          │
│   GitHubClient, GitRepository           │
└────────┬────────────────┬───────────────┘
         │                │
         ▼                ▼
┌────────────────┐  ┌──────────────────┐
│  GitHub API    │  │   Git (libgit2)  │
│   (PyGithub)   │  │    (pygit2)      │
└────────────────┘  └──────────────────┘
```

### Directory Structure

```
github_desktop/
├── core/              # Core business logic
│   ├── github_client.py   # GitHub API wrapper
│   └── git_operations.py  # Git operations wrapper
├── ui/                # User interface components
│   ├── main_window.py     # Main application window
│   ├── auth_dialog.py     # Authentication dialog
│   ├── clone_dialog.py    # Clone repository dialog
│   └── commit_dialog.py   # Commit creation dialog
├── utils/             # Utility functions
│   └── theme.py           # Theme and styling
├── resources/         # Application resources
│   └── (icons, images, etc.)
└── main.py           # Application entry point
```

## Core Components

### 1. GitHubClient (`core/github_client.py`)

Handles all GitHub API operations.

**Key Methods:**
- `authenticate(token)` - Authenticate with GitHub
- `get_user()` - Get authenticated user info
- `get_user_repos()` - List user repositories
- `get_repository(full_name)` - Get specific repository
- `get_pull_requests(repo)` - List pull requests
- `create_pull_request(...)` - Create a PR

**Usage Example:**
```python
client = GitHubClient()
if client.authenticate("ghp_xxx"):
    repos = client.get_user_repos()
    for repo in repos:
        print(repo.full_name)
```

### 2. GitRepository (`core/git_operations.py`)

Handles all Git operations on local repositories.

**Key Methods:**
- `clone(url, path)` - Clone repository
- `get_status()` - Get repository status
- `get_branches()` - List branches
- `checkout_branch(name)` - Switch branches
- `create_branch(name)` - Create new branch
- `stage_files(files)` - Stage files
- `commit(message, author, email)` - Create commit
- `pull()` - Pull from remote
- `push()` - Push to remote
- `get_commit_history()` - Get commit log
- `get_diff()` - Get diff for changes

**Usage Example:**
```python
repo = GitRepository("/path/to/repo")
if repo.is_valid:
    status = repo.get_status()
    repo.stage_all()
    repo.commit("My commit", "User", "user@email.com")
    repo.push()
```

### 3. MainWindow (`ui/main_window.py`)

Main application window with all UI components.

**Key Components:**
- Repository list (left panel)
- Repository details (right panel)
- Changes tab with diff viewer
- History tab with commit log
- Menu bar with actions
- Status bar for feedback

**Signals and Slots:**
PyQt6 uses signals and slots for event handling:
```python
button.clicked.connect(self.on_button_clicked)
```

## Adding New Features

### Example: Adding a New Menu Item

1. **Define the action** in `create_menu_bar()`:
```python
new_action = QAction("My Feature", self)
new_action.setShortcut("Ctrl+M")
new_action.triggered.connect(self.my_feature)
menu.addAction(new_action)
```

2. **Implement the handler**:
```python
def my_feature(self):
    """Handle my feature."""
    if not self.current_repo:
        return
    # Implementation here
```

### Example: Adding a New Dialog

1. **Create dialog class** in `ui/my_dialog.py`:
```python
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton

class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("My Dialog")
        layout = QVBoxLayout(self)
        # Add widgets
        
    def get_result(self):
        return self.result_value
```

2. **Use the dialog**:
```python
from github_desktop.ui.my_dialog import MyDialog

def show_my_dialog(self):
    dialog = MyDialog(self)
    if dialog.exec():
        result = dialog.get_result()
        # Use result
```

### Example: Adding Git Operation

Add to `core/git_operations.py`:

```python
def my_git_operation(self, param: str) -> bool:
    """
    My custom Git operation.
    
    Args:
        param: Parameter description
        
    Returns:
        True if successful, False otherwise
    """
    if not self._repo:
        return False
    
    try:
        # Implementation using pygit2
        return True
    except Exception as e:
        print(f"Operation failed: {e}")
        return False
```

## Styling and Theming

### Modifying Styles

Edit `utils/theme.py`:

```python
# Add new color
NEW_COLOR = "#abcdef"

# Update stylesheet
def get_stylesheet() -> str:
    return """
        QMyWidget {
            background-color: #abcdef;
        }
    """
```

### Applying Custom Styles

In any widget:
```python
widget.setStyleSheet("background-color: #abcdef;")
```

## Testing

### Manual Testing Checklist

- [ ] Authentication with valid/invalid token
- [ ] Clone public/private repository
- [ ] Add local repository
- [ ] View commit history
- [ ] Create commit with changes
- [ ] Create and switch branches
- [ ] Pull from remote
- [ ] Push to remote
- [ ] Handle errors gracefully
- [ ] Keyboard shortcuts work
- [ ] UI is responsive

### Testing with Different Repositories

Test with:
- Empty repositories
- Small repositories (< 100 commits)
- Large repositories (> 1000 commits)
- Repositories with binary files
- Repositories with conflicts

## Debugging

### Enable Debug Logging

Add to `main.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Common Issues

**Issue: PyQt6 import errors**
```bash
pip install --upgrade PyQt6
```

**Issue: pygit2 build fails**
```bash
sudo apt-get install libgit2-dev python3-dev
```

**Issue: Keyring errors**
```bash
sudo apt-get install gnome-keyring
```

### Running in Debug Mode

```bash
python3 -m pdb -m github_desktop.main
```

## Performance Optimization

### Tips for Large Repositories

1. **Limit commit history**:
```python
commits = repo.get_commit_history(limit=50)  # Instead of 100+
```

2. **Lazy loading**:
Load data only when needed, not all at once.

3. **Background threads**:
Use QThread for long operations:
```python
from PyQt6.QtCore import QThread

class WorkerThread(QThread):
    def run(self):
        # Long operation
        pass
```

## Code Style Guidelines

### Python Style
- Follow PEP 8
- Use type hints
- Document with docstrings
- Maximum line length: 100 characters

### Docstring Format
```python
def function(param1: str, param2: int) -> bool:
    """
    Short description.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
    """
    pass
```

### Import Order
1. Standard library
2. Third-party packages
3. Local modules

```python
import os
from pathlib import Path

from PyQt6.QtWidgets import QWidget
import pygit2

from github_desktop.core import GitRepository
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

### Pull Request Checklist

- [ ] Code follows style guidelines
- [ ] Added docstrings to new functions
- [ ] Tested manually
- [ ] Updated documentation
- [ ] No security vulnerabilities introduced

## Resources

### Documentation
- [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [pygit2 Documentation](https://www.pygit2.org/)
- [PyGithub Documentation](https://pygithub.readthedocs.io/)

### Tools
- **Qt Designer**: GUI design tool for PyQt
- **Git**: Command-line Git for reference
- **GitHub API**: REST API documentation

## License

MIT License - See [LICENSE](LICENSE) file for details.
