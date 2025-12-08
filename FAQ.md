# Frequently Asked Questions (FAQ)

## Installation & Setup

### Q: What are the system requirements?
**A:** 
- Ubuntu 20.04 or later (or any modern Linux distribution)
- Python 3.8 or higher
- 2GB RAM minimum (4GB recommended)
- 500MB disk space

### Q: Can I use this on other Linux distributions?
**A:** Yes! While optimized for Ubuntu, it works on:
- Debian-based distributions (Mint, Pop!_OS, etc.)
- Fedora, RHEL, CentOS
- Arch Linux
- Other distributions with Python 3.8+ and Qt6

### Q: Does this work on Windows or macOS?
**A:** Currently, it's designed for Linux. However, the code is mostly cross-platform and could be adapted.

### Q: How do I update to the latest version?
**A:**
```bash
cd GithubDesktopLinux
git pull origin main
./install.sh
```

## Authentication & Security

### Q: Is my Personal Access Token secure?
**A:** Yes! We use your system's keyring (same as your password manager) to securely store tokens. The token is never saved in plain text.

### Q: What permissions does the token need?
**A:** Minimum required scopes:
- `repo` - Access repositories
- `user` - Read user profile
- `workflow` - Manage GitHub Actions (optional but recommended)

### Q: Can I use SSH instead of HTTPS?
**A:** Yes! When cloning, you can use SSH URLs (git@github.com:user/repo.git). Make sure your SSH keys are set up in GitHub.

### Q: How do I log out?
**A:** Currently, you can remove the stored token by deleting it from your system keyring or reinstalling. A proper logout feature is planned for v1.1.

## Features & Usage

### Q: Can I work with multiple GitHub accounts?
**A:** Currently, one account at a time. Multiple account support is planned for v1.1.

### Q: Does it support GitLab or Bitbucket?
**A:** Not yet. GitLab and Bitbucket support are planned for v2.0.

### Q: Can I create pull requests?
**A:** Basic PR support is included. Full PR creation and review features are planned for v1.2.

### Q: Does it support Git LFS?
**A:** Git LFS support is planned for v1.1.

### Q: Can I resolve merge conflicts in the UI?
**A:** Visual merge conflict resolution is planned for v1.1. Currently, use your preferred text editor or command-line tools.

### Q: Does it work with private repositories?
**A:** Yes! As long as your Personal Access Token has the appropriate permissions.

### Q: Can I push to protected branches?
**A:** If you have the necessary permissions in GitHub, yes. The app respects GitHub's branch protection rules.

## Troubleshooting

### Q: The app won't start - what should I check?
**A:**
1. Check Python version: `python3 --version` (needs 3.8+)
2. Verify installation: `pip list | grep -E "PyQt6|pygit2"`
3. Check for errors: Run `python3 -m github_desktop.main` from terminal
4. Review logs in `~/.local/share/github-desktop/logs/`

### Q: I get "Authentication Failed" - what's wrong?
**A:**
1. Verify your token hasn't expired
2. Check you copied the entire token (they start with `ghp_`)
3. Ensure you selected the correct scopes when creating the token
4. Try generating a new token

### Q: Clone/Pull/Push operations fail - why?
**A:**
1. Check your internet connection
2. Verify you have access to the repository
3. For private repos, ensure your token has `repo` scope
4. Check if you're behind a proxy or firewall

### Q: The UI looks different from screenshots - why?
**A:** The app adapts to your system theme. You can also try switching between light and dark themes in your system settings.

### Q: Changes aren't showing up - what's happening?
**A:**
1. Click the refresh button (↻) in the repository list
2. Make sure you've saved your files
3. Check the repository folder location is correct
4. Ensure the `.git` folder exists in the repository

### Q: I can't see my repositories - why?
**A:**
1. Verify authentication is successful
2. Check that repositories exist in `~/Documents/GitHub/` or your custom path
3. Click "Add" to add existing local repositories
4. Use "Clone" to download repositories from GitHub

## Performance

### Q: The app is slow - how can I improve it?
**A:**
1. Close unused repositories
2. Limit commit history display (default is 50 commits)
3. Avoid repositories with huge file counts
4. Upgrade your system RAM if possible

### Q: Can I use this with large repositories?
**A:** Yes, but performance depends on:
- Repository size (files and history)
- System resources
- Disk I/O speed
Consider using command-line Git for extremely large repositories (>10GB).

## Contributing & Development

### Q: How can I contribute?
**A:** See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. We welcome:
- Bug reports
- Feature suggestions
- Code contributions
- Documentation improvements
- Testing and feedback

### Q: Where can I report bugs?
**A:** Open an issue at: https://github.com/AreteDriver/GithubDesktopLinux/issues

### Q: What's the development roadmap?
**A:** See [CHANGELOG.md](CHANGELOG.md) for planned features in upcoming versions.

### Q: Can I create plugins or extensions?
**A:** A plugin system is planned for v1.2+. Currently, you can fork and modify the code (it's MIT licensed).

## Miscellaneous

### Q: Is this the official GitHub Desktop?
**A:** No, this is an independent, community-driven project inspired by GitHub Desktop but specifically designed for Linux/Ubuntu.

### Q: How does this compare to other Git GUIs?
**A:** GitHub Desktop for Ubuntu focuses on:
- GitHub integration
- Ubuntu/Linux optimization
- Developer-friendly features
- Clean, modern UI
- Easy installation and use

### Q: Is there a command-line version?
**A:** This is a GUI application. For command-line Git, use the standard `git` command.

### Q: Can I use custom themes?
**A:** Custom themes are planned for v1.2. Currently, the app adapts to your system theme.

### Q: Where are my repositories stored?
**A:** By default: `~/Documents/GitHub/`
You can choose a different location when cloning or adding repositories.

### Q: Does it work offline?
**A:** Local Git operations (commit, branch, etc.) work offline. Operations requiring GitHub (clone, pull, push, browse repos) need internet.

## Still have questions?

- Check the [README.md](README.md) for detailed documentation
- Search existing [GitHub Issues](https://github.com/AreteDriver/GithubDesktopLinux/issues)
- Open a new issue with the `question` label
- Review the [Quick Start Guide](QUICKSTART.md)
