# Changelog

All notable changes to GitHub Desktop for Ubuntu will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-08

### Added
- Initial release of GitHub Desktop for Ubuntu
- Modern PyQt6-based user interface
- GitHub API integration with OAuth support
- Core Git operations (clone, commit, push, pull, fetch)
- Branch management (create, switch, view)
- Repository browser and selector
- Commit history viewer with detailed diffs
- Visual staging area for commits
- Syntax-highlighted diff viewer
- Dark/Light theme support
- Ubuntu desktop integration (launcher, system tray)
- Secure credential storage using system keyring
- Clone repository dialog with GitHub repo browser
- Authentication dialog for Personal Access Tokens
- Keyboard shortcuts for common operations
- Status bar with operation feedback
- Multi-repository support
- Installation script for easy setup
- Comprehensive documentation

### Features
- **UI/UX**: Clean, GitHub-inspired interface with responsive layout
- **Git Operations**: Full Git workflow support through libgit2
- **GitHub Integration**: Browse, clone, and manage GitHub repositories
- **Developer Tools**: Syntax highlighting, monospace fonts, keyboard shortcuts
- **Ubuntu Integration**: Native launcher, notifications, theme support
- **Security**: Secure token storage with system keyring

### Technical
- Python 3.8+ support
- PyQt6 for modern GUI
- pygit2 for Git operations
- PyGithub for GitHub API
- Cross-platform design (Linux-focused)
- Modular architecture for easy extension

## [Unreleased]

### Planned for 1.1.0
- Visual merge conflict resolution
- Git LFS support
- Advanced stash management
- Repository search functionality
- Multiple account support
- Improved error handling and recovery

### Planned for 1.2.0
- Pull request creation and review
- Issue creation and management
- Code review tools
- Git hooks integration
- Custom theme support
- Plugin system foundation

### Planned for 2.0.0
- GitLab integration
- Bitbucket integration
- CI/CD pipeline visualization
- Team collaboration features
- Advanced plugin system

---

[1.0.0]: https://github.com/AreteDriver/GithubDesktopLinux/releases/tag/v1.0.0
