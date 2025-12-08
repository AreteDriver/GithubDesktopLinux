# Contributing to GitHub Desktop Linux

Thank you for your interest in contributing to GitHub Desktop Linux! This document provides guidelines and instructions for contributing.

## Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/GithubDesktopLinux.git
   cd GithubDesktopLinux
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Start Development**
   ```bash
   npm start
   ```

## Project Structure

- `src/main/` - Electron main process (Node.js)
- `src/renderer/` - Electron renderer process (React + TypeScript)
  - `components/` - React components
  - `utils/` - Utility functions and API wrappers
  - `styles/` - CSS stylesheets
- `public/` - Static assets

## Development Workflow

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
   - Write clean, well-documented code
   - Follow existing code style and conventions
   - Test your changes thoroughly

3. **Build and Test**
   ```bash
   npm run build
   npm start
   ```

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: Add your feature description"
   ```

   Follow [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat:` - New feature
   - `fix:` - Bug fix
   - `docs:` - Documentation changes
   - `style:` - Code style changes (formatting)
   - `refactor:` - Code refactoring
   - `test:` - Adding tests
   - `chore:` - Maintenance tasks

5. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a Pull Request on GitHub.

## Code Style

- Use TypeScript for new code
- Follow existing formatting conventions
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and small

## Testing

- Test all Git operations with real repositories
- Verify UI changes in different scenarios
- Test template application
- Check for memory leaks in long-running operations

## Adding Features

### Adding a New Template

Edit `src/renderer/utils/templates.ts` and add your template to the `repoTemplates` array:

```typescript
{
  id: 'my-template',
  name: 'My Template',
  description: 'Description of my template',
  files: {
    'file1.txt': 'content',
    'file2.txt': 'content',
  },
  gitignore: 'patterns\nto\nignore',
}
```

### Adding a Git Operation

1. Add IPC handler in `src/main/index.js`
2. Add API method in `src/renderer/utils/gitApi.ts`
3. Use the API in your component

## Reporting Issues

When reporting issues, please include:

- OS and version
- Node.js and npm versions
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Error messages or logs

## Feature Requests

We welcome feature requests! Please:

- Check existing issues first
- Describe the use case
- Explain why it would be useful
- Consider contributing the implementation

## Pull Request Guidelines

- Keep PRs focused on a single feature or fix
- Update documentation if needed
- Add screenshots for UI changes
- Ensure the build passes
- Respond to review feedback promptly

## Questions?

Feel free to open an issue for questions or discussions.

Thank you for contributing! 🎉
