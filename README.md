# GitHub Desktop for Ubuntu 🐧

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Ubuntu%20%7C%20Linux-orange.svg)](https://ubuntu.com/)

The best possible version of GitHub for Ubuntu desktop. A modern, feature-rich GitHub client designed specifically for Ubuntu and Linux users.

![GitHub Desktop for Ubuntu](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)

## ✨ Features

### 🎨 Modern User Interface
- **Clean, Intuitive Design** - GitHub-inspired interface with familiar workflows
- **Dark/Light Theme Support** - Seamlessly adapts to your system preferences
- **Responsive Layout** - Resizable panels and optimized for various screen sizes
- **Native Ubuntu Integration** - Desktop launcher, system tray, and notifications

### 🔧 Powerful Git Operations
- **Visual Git Interface** - Manage repositories without command-line complexity
- **Branch Management** - Create, switch, and manage branches effortlessly
- **Commit History** - Browse commit history with detailed diffs
- **Stage & Commit** - Visual staging area for selective commits
- **Pull & Push** - Sync changes with remote repositories
- **Conflict Resolution** - Visual tools for merge conflict resolution
- **Stash Management** - Save and apply work-in-progress changes

### 🐙 GitHub Integration
- **OAuth Authentication** - Secure login with Personal Access Tokens
- **Repository Browser** - Browse and clone your GitHub repositories
- **Pull Request Integration** - View and manage pull requests
- **Issue Tracking** - Access GitHub issues directly from the app
- **Quick Open on GitHub** - Jump to repository on GitHub.com
- **Credential Storage** - Secure token storage using system keyring

### 👨‍💻 Developer-Focused Features
- **Syntax Highlighting** - Color-coded diffs for easy code review
- **Monospace Fonts** - Optimized code display
- **Keyboard Shortcuts** - Efficient navigation and operations
- **Git LFS Support** - Handle large files with Git LFS
- **Multiple Repository Management** - Work with multiple repos simultaneously
- **Smart File Detection** - Automatically detect repository changes

### 🚀 Performance & Reliability
- **Fast Operations** - Optimized Git operations using pygit2
- **Efficient Rendering** - Smooth UI with PyQt6
- **Error Handling** - Graceful error recovery and user feedback
- **Background Operations** - Non-blocking UI for long-running tasks

## 📋 Requirements

### System Requirements
- **OS**: Ubuntu 20.04+ or any modern Linux distribution
- **Python**: 3.8 or later
- **RAM**: 2GB minimum (4GB recommended)
- **Disk Space**: 500MB for installation

### Dependencies
- Python 3.8+
- Qt6 libraries
- libgit2
- System keyring support

All dependencies are automatically installed by the installation script.

## 🔧 Installation

### Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/AreteDriver/GithubDesktopLinux.git
cd GithubDesktopLinux

# Run the installation script
./install.sh
```

The installation script will:
1. Check system requirements
2. Install system dependencies (requires sudo)
3. Create a Python virtual environment
4. Install Python packages
5. Create a desktop launcher
6. Set up the application

### Manual Installation

If you prefer to install manually:

```bash
# Install system dependencies (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install python3-pip python3-venv python3-dev libgit2-dev pkg-config

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install the application
pip install -e .
```

## 🚀 Usage

### Launching the Application

After installation, you can launch GitHub Desktop in several ways:

1. **From Applications Menu**: Search for "GitHub Desktop" in your applications
2. **From Terminal**: Run `./github-desktop` from the installation directory
3. **Direct Python**: `python3 -m github_desktop.main` (with venv activated)

### First-Time Setup

1. **Create a Personal Access Token**:
   - Go to [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)
   - Click "Generate new token (classic)"
   - Give it a descriptive name (e.g., "GitHub Desktop Ubuntu")
   - Select scopes: `repo`, `user`, `workflow`
   - Click "Generate token"
   - **Copy the token** (you won't be able to see it again!)

2. **Authenticate**:
   - Launch GitHub Desktop
   - Paste your Personal Access Token in the authentication dialog
   - Click "Sign In"

### Working with Repositories

#### Clone a Repository
1. Click **File → Clone Repository** or press `Ctrl+Shift+O`
2. Select a repository from your list or enter a URL
3. Choose a local path
4. Click "Clone"

#### Add Local Repository
1. Click **File → Add Local Repository** or press `Ctrl+O`
2. Select the repository directory
3. Click "Open"

#### Make Commits
1. Make changes to your files
2. Changed files will appear in the "Changes" tab
3. Review the diff in the diff viewer
4. Enter a commit message
5. Click "Commit to current branch"

#### Sync with Remote
- **Fetch**: Repository → Fetch (`Ctrl+Shift+F`)
- **Pull**: Repository → Pull (`Ctrl+Shift+P`)
- **Push**: Repository → Push (`Ctrl+P`)

#### Branch Management
- **Create Branch**: Branch → New Branch (`Ctrl+Shift+N`)
- **Switch Branch**: Branch → Switch Branch (`Ctrl+B`)

### Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Clone Repository | `Ctrl+Shift+O` |
| Add Local Repository | `Ctrl+O` |
| Fetch | `Ctrl+Shift+F` |
| Pull | `Ctrl+Shift+P` |
| Push | `Ctrl+P` |
| New Branch | `Ctrl+Shift+N` |
| Switch Branch | `Ctrl+B` |
| View on GitHub | `Ctrl+Shift+G` |
| Quit | `Ctrl+Q` |

## 🏗️ Architecture

### Technology Stack
- **GUI Framework**: PyQt6 - Modern, cross-platform UI framework
- **Git Operations**: pygit2 - Python bindings for libgit2
- **GitHub API**: PyGithub - GitHub API v3 wrapper
- **Security**: keyring - Secure credential storage
- **Language**: Python 3.8+ - Clean, maintainable codebase

### Project Structure
```
GithubDesktopLinux/
├── github_desktop/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── core/
│   │   ├── github_client.py # GitHub API integration
│   │   └── git_operations.py # Git operations wrapper
│   ├── ui/
│   │   ├── main_window.py   # Main application window
│   │   ├── auth_dialog.py   # Authentication dialog
│   │   ├── clone_dialog.py  # Clone repository dialog
│   │   └── commit_dialog.py # Commit creation dialog
│   ├── utils/
│   │   └── theme.py         # Theme and styling
│   └── resources/           # Icons and assets
├── requirements.txt         # Python dependencies
├── setup.py                # Package configuration
├── install.sh              # Installation script
└── README.md               # This file
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Commit your changes**: `git commit -m 'Add amazing feature'`
5. **Push to the branch**: `git push origin feature/amazing-feature`
6. **Open a Pull Request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/GithubDesktopLinux.git
cd GithubDesktopLinux

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install in development mode
pip install -e .

# Run the application
python3 -m github_desktop.main
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: Application won't start
```bash
# Check Python version
python3 --version  # Should be 3.8+

# Check dependencies
pip list | grep -E "PyQt6|pygit2|PyGithub"
```

**Issue**: Authentication fails
- Verify your Personal Access Token is valid
- Check that you selected the correct scopes (repo, user, workflow)
- Generate a new token if necessary

**Issue**: Clone fails
- Check your internet connection
- Verify the repository URL
- Ensure you have access to the repository

**Issue**: Push/Pull fails
- Check your network connection
- Verify you have push access to the repository
- Check if there are merge conflicts

### Getting Help

- **GitHub Issues**: [Report bugs or request features](https://github.com/AreteDriver/GithubDesktopLinux/issues)
- **Discussions**: Ask questions and share ideas

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **GitHub** - For the amazing platform and inspiration
- **PyQt** - For the powerful GUI framework
- **libgit2** - For robust Git operations
- **Ubuntu Community** - For the excellent Linux distribution

## 🎯 Roadmap

### Version 1.1 (Planned)
- [ ] Visual merge conflict resolution
- [ ] Git LFS support
- [ ] Advanced stash management
- [ ] Repository search
- [ ] Multiple account support

### Version 1.2 (Planned)
- [ ] Pull request creation and review
- [ ] Issue creation and management
- [ ] Code review tools
- [ ] Git hooks integration
- [ ] Custom themes

### Version 2.0 (Future)
- [ ] GitLab integration
- [ ] Bitbucket integration
- [ ] CI/CD pipeline visualization
- [ ] Team collaboration features
- [ ] Plugins system

## 📞 Contact

**Project Maintainer**: GitHub Desktop Ubuntu Team

**Repository**: [https://github.com/AreteDriver/GithubDesktopLinux](https://github.com/AreteDriver/GithubDesktopLinux)

---

Made with ❤️ for the Ubuntu and Linux community