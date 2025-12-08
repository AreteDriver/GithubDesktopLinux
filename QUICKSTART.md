# Quick Start Guide

Get up and running with GitHub Desktop for Ubuntu in 5 minutes!

## Installation (2 minutes)

```bash
# 1. Clone the repository
git clone https://github.com/AreteDriver/GithubDesktopLinux.git
cd GithubDesktopLinux

# 2. Run the installer
./install.sh
```

The installer will:
- Install system dependencies (requires sudo)
- Set up Python environment
- Install the application
- Create desktop launcher

## First Launch (2 minutes)

### 1. Get Your GitHub Token

Visit: https://github.com/settings/tokens/new

- **Token name**: `GitHub Desktop Ubuntu`
- **Scopes**: Check `repo`, `user`, `workflow`
- Click **Generate token**
- **Copy the token** (you won't see it again!)

### 2. Launch the App

Find "GitHub Desktop" in your applications menu or run:
```bash
./github-desktop
```

### 3. Sign In

- Paste your Personal Access Token
- Click "Sign In"
- You're ready to go! 🎉

## Your First Repository (1 minute)

### Option A: Clone an Existing Repo

1. Click **File → Clone Repository** (or `Ctrl+Shift+O`)
2. Select a repository from your list OR enter a URL
3. Choose where to save it
4. Click **Clone**

### Option B: Add a Local Repo

1. Click **File → Add Local Repository** (or `Ctrl+O`)
2. Select your repository folder
3. Click **Open**

## Make Your First Commit

1. **Make changes** to files in your repository
2. **See changes** appear in the "Changes" tab
3. **Review the diff** in the bottom panel
4. **Write a message** describing your changes
5. **Click "Commit to current branch"**
6. **Push** with `Ctrl+P` or the Push button

## Common Tasks

| Task | How To |
|------|--------|
| **Create a branch** | Branch → New Branch (`Ctrl+Shift+N`) |
| **Switch branches** | Branch → Switch Branch (`Ctrl+B`) |
| **Pull changes** | Repository → Pull (`Ctrl+Shift+P`) |
| **Push changes** | Repository → Push (`Ctrl+P`) |
| **View on GitHub** | Repository → View on GitHub (`Ctrl+Shift+G`) |

## Keyboard Shortcuts Cheat Sheet

```
Ctrl+Shift+O    Clone Repository
Ctrl+O          Add Local Repository
Ctrl+Shift+N    New Branch
Ctrl+B          Switch Branch
Ctrl+Shift+P    Pull
Ctrl+P          Push
Ctrl+Shift+G    View on GitHub
Ctrl+Q          Quit
```

## Tips & Tricks

### 📝 Writing Good Commit Messages
- **First line**: Brief summary (50 chars or less)
- **Blank line**
- **Details**: Why you made the change

### 🔄 Keeping in Sync
- **Fetch** regularly to see remote changes
- **Pull** before starting new work
- **Push** your commits to share them

### 🌿 Working with Branches
- Create a branch for each feature/fix
- Keep `main` clean and stable
- Merge when ready

### ⚡ Productivity
- Use keyboard shortcuts
- Stage specific files for granular commits
- Review diffs before committing

## Need Help?

- 📖 **Full Documentation**: See [README.md](README.md)
- 🐛 **Report Issues**: [GitHub Issues](https://github.com/AreteDriver/GithubDesktopLinux/issues)
- 💬 **Ask Questions**: Open a discussion

## What's Next?

Now that you're set up, explore:
- Browse commit history
- Try different branches
- Experiment with the UI
- Customize your workflow

**Happy coding!** 🚀
