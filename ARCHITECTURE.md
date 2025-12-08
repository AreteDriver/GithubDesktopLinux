# Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    GitHub Desktop Linux                      │
│                      Electron App                            │
└─────────────────────────────────────────────────────────────┘
                            │
                ┌───────────┴───────────┐
                │                       │
        ┌───────▼────────┐    ┌────────▼────────┐
        │  Main Process  │    │ Renderer Process │
        │   (Node.js)    │    │  (React + TS)   │
        └───────┬────────┘    └────────┬─────────┘
                │                      │
                │   ◄──── IPC ────►    │
                │   (contextBridge)    │
                │                      │
    ┌───────────▼──────────┐          │
    │   Git Operations     │          │
    │   - simple-git       │          │
    │   - File System      │          │
    │   - Dialog APIs      │          │
    └──────────────────────┘          │
                               ┌──────▼──────────┐
                               │   UI Components │
                               │   - App.tsx     │
                               │   - Components  │
                               │   - Utils       │
                               └─────────────────┘
```

## Component Architecture

```
┌──────────────────────────────────────────────────────────┐
│                        App.tsx                           │
│  (Main Application Component)                            │
│                                                          │
│  State Management:                                       │
│  - Repository path                                       │
│  - Git status, branches, log                            │
│  - Selected files, staged files                         │
│  - Notifications                                         │
└────────┬──────────────────────────────────┬─────────────┘
         │                                  │
    ┌────▼────┐  ┌──────────┐  ┌──────────▼──────────┐
    │ Sidebar │  │ Toolbar  │  │   Content Area      │
    └─────────┘  └──────────┘  └─────────┬───────────┘
                                          │
                    ┌─────────────────────┼─────────────────┐
                    │                     │                 │
            ┌───────▼────────┐  ┌────────▼──────┐  ┌──────▼──────┐
            │  Changes Tab   │  │ History Tab   │  │ Branches Tab│
            └───────┬────────┘  └────────┬──────┘  └─────────────┘
                    │                    │
        ┌───────────┴─────────┐         │
        │                     │         │
┌───────▼────────┐  ┌─────────▼──────┐ │
│  CommitForm    │  │  DiffViewer    │ │
│  - AI Suggest  │  │  - Syntax      │ │
│  - Stage/Commit│  │  - Color Code  │ │
└────────────────┘  └────────────────┘ │
                                       │
                         ┌─────────────▼─────────┐
                         │ BranchVisualization   │
                         │ - Commit Timeline     │
                         │ - Branch Graph        │
                         └───────────────────────┘
```

## Data Flow

```
User Action
    │
    ▼
React Component
    │
    ▼
gitApi.ts (IPC Wrapper)
    │
    ▼
window.electronAPI (contextBridge)
    │
    ▼
IPC Channel (secure)
    │
    ▼
Main Process Handler
    │
    ▼
simple-git / File System
    │
    ▼
Git Repository / Local Files
    │
    ▼
Response ──► IPC Return ──► Component Update ──► UI Refresh
```

## Security Architecture

```
┌─────────────────────────────────────────────────────┐
│              Renderer Process (Isolated)            │
│  ┌───────────────────────────────────────────┐     │
│  │           React Application               │     │
│  │  - No Node.js access                      │     │
│  │  - No require()                           │     │
│  │  - Only window.electronAPI                │     │
│  └───────────────┬───────────────────────────┘     │
│                  │                                  │
│                  ▼                                  │
│  ┌───────────────────────────────────────────┐     │
│  │        Preload Script (Bridge)            │     │
│  │  - contextBridge.exposeInMainWorld()      │     │
│  │  - Whitelisted APIs only                  │     │
│  │  - No raw IPC access                      │     │
│  └───────────────┬───────────────────────────┘     │
└──────────────────┼──────────────────────────────────┘
                   │ Secure IPC
┌──────────────────▼──────────────────────────────────┐
│              Main Process (Privileged)              │
│  ┌───────────────────────────────────────────┐     │
│  │          IPC Handlers                     │     │
│  │  - Validate all inputs                    │     │
│  │  - Execute Git operations                 │     │
│  │  - File system access                     │     │
│  │  - Dialog operations                      │     │
│  └───────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────┘
```

## Feature Implementation

### 1. Modern UI
```
App.css ─────► Styled Components
   │              │
   ├─► Dark Theme (#1e1e1e)
   ├─► Blue Accents (#0e639c)
   ├─► VS Code Style
   └─► Responsive Layout
```

### 2. Branch Visualization
```
Git Log API ──► BranchVisualization.tsx
                      │
                      ├─► Commit Nodes
                      ├─► Connection Lines
                      ├─► Metadata Display
                      └─► Timeline Layout
```

### 3. AI Commit Suggestions
```
Staged Changes ──► Git Diff ──► AI Analysis ──► Suggestions
                                     │
                        ├─── File Patterns
                        ├─── Change Ratio
                        ├─── Conventional Commits
                        └─── Context Detection
```

### 4. Integrated Diff Viewer
```
File Selection ──► Git Diff ──► DiffViewer.tsx
                                      │
                                      ├─► Parse Lines
                                      ├─► Color Code
                                      ├─► (+) Green
                                      ├─► (-) Red
                                      └─► Context Gray
```

### 5. Repository Templates
```
Template Selection ──► templates.ts ──► File Creation
                             │
                ├─── Node.js + TypeScript
                ├─── React Application
                ├─── Python Project
                └─── Basic Repository
```

## Technology Stack Details

### Frontend (Renderer)
- **React 18**: UI framework with hooks
- **TypeScript 5**: Type safety
- **CSS3**: Custom styling
- **Webpack 5**: Module bundling

### Backend (Main)
- **Electron 28**: Desktop framework
- **Node.js 20**: Runtime
- **simple-git 3**: Git operations
- **IPC**: Inter-process communication

### Development
- **npm**: Package management
- **TypeScript Compiler**: Type checking
- **Webpack**: Build system
- **electron-builder**: Packaging

## Build Process

```
Source Files (TypeScript + React)
        │
        ▼
TypeScript Compiler (tsc)
        │
        ▼
Webpack Bundler
        │
        ├─► Bundle JavaScript
        ├─► Process CSS
        ├─► Generate HTML
        └─► Optimize Assets
        │
        ▼
dist/ Directory
        │
        ├─► renderer.js (166KB)
        ├─► index.html
        └─► assets
        │
        ▼
Electron Builder
        │
        ├─► AppImage (Linux)
        └─► .deb Package (Debian/Ubuntu)
```

## Git Operations Flow

```
User Interface
    │
    ├─► git:status ──────► Get modified files
    ├─► git:log ─────────► Get commit history
    ├─► git:branches ────► List branches
    ├─► git:diff ────────► Get file changes
    ├─► git:commit ──────► Create commit
    ├─► git:add ─────────► Stage files
    ├─► git:checkout ────► Switch branches
    ├─► git:pull ────────► Fetch & merge
    └─► git:push ────────► Upload commits
```

## State Management

```
App Component (Root State)
    │
    ├─► repoPath: string
    ├─► status: GitStatus
    ├─► branches: GitBranches
    ├─► log: GitLog
    ├─► selectedFile: string | null
    ├─► diff: string
    ├─► activeTab: 'changes' | 'history' | 'branches'
    ├─► stagedFiles: string[]
    ├─► notifications: Notification[]
    └─► showTemplateModal: boolean
```

## File Structure

```
GithubDesktopLinux/
├── src/
│   ├── main/
│   │   ├── index.js           # Main process entry
│   │   └── preload.js         # Security bridge
│   └── renderer/
│       ├── components/
│       │   ├── BranchVisualization.tsx
│       │   ├── CommitForm.tsx
│       │   ├── DiffViewer.tsx
│       │   └── TemplateModal.tsx
│       ├── utils/
│       │   ├── gitApi.ts      # IPC wrapper
│       │   └── templates.ts   # Template definitions
│       ├── styles/
│       │   └── App.css        # Global styles
│       ├── App.tsx            # Main component
│       └── index.tsx          # Entry point
├── public/
│   └── index.html             # HTML template
├── dist/                      # Build output
├── package.json               # Dependencies
├── tsconfig.json              # TypeScript config
├── webpack.config.js          # Build config
├── README.md                  # User documentation
├── CONTRIBUTING.md            # Developer guide
├── FEATURES.md                # Feature details
├── PROJECT_SUMMARY.md         # Project overview
└── LICENSE                    # MIT License
```

---

This architecture ensures:
- ✅ Security through isolation
- ✅ Maintainability through separation of concerns
- ✅ Performance through optimized builds
- ✅ Scalability through modular design
- ✅ Type safety through TypeScript
- ✅ User experience through modern UI patterns
