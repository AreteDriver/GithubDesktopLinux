# Quick Start Guide

Get started with GitHub Desktop Linux in 5 minutes!

## Prerequisites

- Linux operating system (Ubuntu, Debian, Fedora, Arch, etc.)
- Node.js 20.x or higher ([Download](https://nodejs.org/))
- npm 10.x or higher (comes with Node.js)
- Git installed on your system

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AreteDriver/GithubDesktopLinux.git
cd GithubDesktopLinux
```

### 2. Install Dependencies

```bash
npm install
```

This will install all required packages including Electron, React, TypeScript, and build tools.

### 3. Run the Application

```bash
npm start
```

The application will launch in development mode with developer tools enabled.

## First Steps

### Opening a Repository

1. When the app starts, you'll see the welcome screen
2. Click **"Open Repository"**
3. Navigate to any Git repository on your system
4. Select the repository folder
5. The app will load your repository data

### Making a Commit

1. Navigate to the **"Changes"** tab (default view)
2. You'll see a list of modified files
3. Click **"Stage"** next to files you want to commit
4. Review the AI-generated commit message suggestions
5. Click a suggestion or write your own message
6. Click **"Commit"** to save your changes

### Viewing History

1. Click the **"History"** tab
2. See a visual timeline of all your commits
3. Each commit shows:
   - Commit message
   - Author name
   - Date and time
   - Short hash

### Managing Branches

1. Click the **"Branches"** tab
2. See all available branches
3. Current branch is marked with a star (★)
4. Click **"Switch"** to change branches

### Using Templates

1. Click **"Apply Template"** in the sidebar
2. Choose from available templates:
   - Node.js + TypeScript
   - React Application
   - Python Project
   - Basic Repository
3. Template files are created automatically
4. Stage and commit the new files

## Quick Actions

Available from the sidebar:

- **Pull**: Fetch and merge changes from remote
- **Push**: Upload your local commits to remote
- **Apply Template**: Initialize repository with a template

## Keyboard Shortcuts

Currently, all operations are mouse-driven. Keyboard shortcuts are planned for a future release.

## Tips & Tricks

### AI Commit Messages

The AI suggestion system works best when you:
- Stage related changes together
- Make focused commits (not too many files at once)
- Let it analyze your diff patterns

### Diff Viewer

- Click any file in the changes list to see its diff
- Green lines = additions
- Red lines = deletions
- Gray lines = context (unchanged)

### Templates

- Templates are great for starting new projects
- You can customize templates in `src/renderer/utils/templates.ts`
- Add your own organization-specific templates

## Building for Distribution

### Development Build

```bash
npm run build
```

Creates optimized production bundle in `dist/` folder.

### Linux Package

```bash
npm run package:linux
```

Creates:
- AppImage (universal Linux package)
- .deb package (Debian/Ubuntu)

Packages are created in the `dist/` folder and can be distributed to other users.

## Troubleshooting

### Application Won't Start

```bash
# Clean install
rm -rf node_modules dist
npm install
npm start
```

### Git Operations Fail

- Ensure Git is installed: `git --version`
- Check repository path is valid
- Verify you have permissions to access the repository

### Build Errors

```bash
# Check Node.js version (needs 20.x+)
node --version

# Update dependencies
npm update
```

### Can't Open Repository

- Make sure the folder is a Git repository (has `.git/` folder)
- Check file permissions
- Try with a different repository to isolate the issue

## Next Steps

- Read the [README.md](README.md) for complete documentation
- Check [FEATURES.md](FEATURES.md) for detailed feature explanations
- See [CONTRIBUTING.md](CONTRIBUTING.md) if you want to contribute
- Review [ARCHITECTURE.md](ARCHITECTURE.md) to understand the codebase

## Getting Help

- Check existing documentation first
- Look for similar issues on GitHub
- Open a new issue with:
  - Your OS and version
  - Node.js version
  - Steps to reproduce
  - Error messages or screenshots

## What's Next?

Try these features:
1. ✅ Open your favorite project
2. ✅ Make some changes
3. ✅ Use AI suggestions for commit messages
4. ✅ View the commit history graph
5. ✅ Try switching branches
6. ✅ Create a new project with a template

---

**Happy coding! 🚀**

Built with ❤️ for the Linux community
