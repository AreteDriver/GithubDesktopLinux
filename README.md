# GitHub Desktop Linux

A modern, feature-rich GitHub Desktop alternative built specifically for Linux. This application provides a beautiful, intuitive interface for Git operations with AI-powered features.

## 🚀 Features

### ✨ Modern UI
- Clean, contemporary dark theme interface
- Intuitive navigation and workflow
- Responsive design optimized for Linux desktop environments
- Professional Visual Studio Code-inspired aesthetics

### 🌳 Branch Visualization
- Visual commit history graph
- Clear branch relationships and merge visualization
- Interactive branch switching
- Commit timeline with detailed metadata

### 🤖 AI Commit Message Suggestions
- Intelligent commit message generation based on changes
- Context-aware suggestions analyzing your diff
- Multiple suggestion options to choose from
- One-click application of suggested messages

### 📊 Integrated Diff Viewer
- Side-by-side diff viewing
- Syntax highlighting for code changes
- Line-by-line change visualization
- Addition/deletion highlighting
- File-by-file diff navigation

### 📋 Repository Templates
- Pre-configured repository templates
- Support for multiple project types:
  - Node.js + TypeScript
  - React Application
  - Python Project
  - Basic Repository
- One-click template application
- Automatic file structure setup

## 🛠️ Installation

### Prerequisites
- Node.js 20.x or higher
- npm 10.x or higher
- Git installed on your system

### Install Dependencies

```bash
npm install
```

## 🏃 Running the Application

### Development Mode

```bash
npm start
```

This will launch the Electron application in development mode with developer tools enabled.

### Build for Production

```bash
npm run build
```

### Package for Linux

Create distributable packages (AppImage and .deb):

```bash
npm run package:linux
```

The packaged applications will be available in the `dist` folder.

## 📖 Usage

### Opening a Repository

1. Click "Open Repository" from the welcome screen
2. Select your Git repository folder
3. The application will load the repository status, branches, and commit history

### Making Commits

1. Navigate to the "Changes" tab
2. Review your modified files
3. Click "Stage" on files you want to commit
4. Review the AI-generated commit message suggestions
5. Select a suggestion or write your own message
6. Click "Commit" to commit your changes

### Viewing History

1. Navigate to the "History" tab
2. View the visual commit timeline
3. See commit messages, authors, and timestamps
4. Explore the branch visualization

### Managing Branches

1. Navigate to the "Branches" tab
2. View all available branches
3. Click "Switch" to change branches
4. Current branch is highlighted with a star (★)

### Using Templates

1. Click "Apply Template" from the sidebar
2. Choose from available templates
3. Template files will be created in your repository
4. Stage and commit the new files

## 🏗️ Architecture

### Technology Stack

- **Electron**: Desktop application framework
- **React**: UI framework
- **TypeScript**: Type-safe development
- **simple-git**: Git operations
- **Webpack**: Module bundler

### Project Structure

```
├── src/
│   ├── main/           # Electron main process
│   │   └── index.js    # Main entry point, IPC handlers
│   └── renderer/       # Electron renderer process
│       ├── components/ # React components
│       │   ├── BranchVisualization.tsx
│       │   ├── CommitForm.tsx
│       │   ├── DiffViewer.tsx
│       │   └── TemplateModal.tsx
│       ├── utils/      # Utility functions
│       │   ├── gitApi.ts
│       │   └── templates.ts
│       ├── styles/     # CSS styles
│       │   └── App.css
│       ├── App.tsx     # Main React component
│       └── index.tsx   # Renderer entry point
├── public/            # Static assets
│   └── index.html
└── package.json       # Dependencies and scripts
```

## 🎨 Features in Detail

### Modern UI
The application features a dark theme with a professional appearance inspired by modern IDEs. The interface is divided into:
- **Sidebar**: Repository info, branch selector, and quick actions
- **Toolbar**: Navigation and refresh controls
- **Tab Navigation**: Switch between Changes, History, and Branches views
- **Content Area**: Main workspace for viewing and interacting with Git data

### Branch Visualization
The commit history is displayed as a visual timeline with:
- Commit nodes connected by lines showing the flow
- Commit messages and metadata
- Author information and timestamps
- Short commit hashes for reference

### AI Commit Messages
The AI suggestion system analyzes your changes and provides intelligent commit messages by:
- Examining the diff to understand the nature of changes
- Detecting file patterns (tests, docs, configs)
- Calculating addition/deletion ratios
- Providing conventional commit format suggestions

### Integrated Diff Viewer
View your changes with a professional diff viewer that:
- Shows additions in green and deletions in red
- Preserves code formatting and structure
- Displays context lines for better understanding
- Updates in real-time when selecting files

### Repository Templates
Quickly scaffold new projects with templates that include:
- Pre-configured package.json
- TypeScript/JavaScript configurations
- Starter code and examples
- Appropriate .gitignore files
- README documentation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📝 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- Built with Electron for cross-platform desktop support
- React for a modern, reactive UI
- simple-git for reliable Git operations
- Inspired by GitHub Desktop but built specifically for Linux users

## 🐛 Troubleshooting

### Application won't start
- Ensure all dependencies are installed: `npm install`
- Check Node.js version: `node --version` (should be 20.x+)
- Try cleaning and rebuilding: `rm -rf node_modules dist && npm install`

### Git operations fail
- Ensure Git is installed and accessible from command line
- Verify the repository path is valid
- Check repository permissions

### Template application fails
- Ensure you have write permissions in the repository directory
- Check that files don't already exist (templates won't overwrite)

## 📮 Contact & Support

For issues, questions, or feature requests, please open an issue on GitHub.

---

**Made with ❤️ for the Linux community**