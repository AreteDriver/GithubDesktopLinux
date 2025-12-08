# Contributing to GitHub Desktop for Ubuntu

Thank you for your interest in contributing to GitHub Desktop for Ubuntu! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect different viewpoints and experiences

## How to Contribute

### Reporting Bugs

Before creating a bug report:
1. Check if the bug has already been reported
2. Check if you're using the latest version
3. Gather relevant information (OS version, Python version, error messages)

When creating a bug report, include:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- System information

### Suggesting Features

We welcome feature suggestions! When suggesting a feature:
- Check if it's already been suggested
- Explain why this feature would be useful
- Provide examples of how it would work
- Consider if it fits the project's scope

### Pull Requests

1. **Fork the repository** and create a branch from `main`
2. **Follow the coding style** used in the project
3. **Write clear commit messages**
4. **Add tests** if applicable
5. **Update documentation** as needed
6. **Test your changes** thoroughly

#### Coding Standards

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and concise
- Comment complex logic

#### Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Example:
```
feat: Add dark theme support

- Implemented dark theme color palette
- Added theme switcher in preferences
- Updated UI components to support theming

Closes #123
```

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/GithubDesktopLinux.git
cd GithubDesktopLinux

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -e .

# Run the application
python3 -m github_desktop.main
```

### Project Structure

```
github_desktop/
├── core/          # Core functionality (Git, GitHub API)
├── ui/            # User interface components
├── utils/         # Utility functions and helpers
└── resources/     # Icons, images, etc.
```

### Testing

While we don't have automated tests yet, please manually test:
- All affected features
- On a clean environment
- With different repository states
- Error cases and edge cases

### Documentation

When adding new features:
- Update README.md if needed
- Add docstrings to new functions/classes
- Update relevant documentation files
- Consider adding examples

## Questions?

Feel free to open an issue with the `question` label if you have any questions about contributing.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
