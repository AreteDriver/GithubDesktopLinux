#!/bin/bash

# GitHub Desktop for Ubuntu - Installation Script

set -e

echo "=========================================="
echo "GitHub Desktop for Ubuntu - Installation"
echo "=========================================="
echo ""

# Check if running on Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo "Error: This script is designed for Linux systems."
    exit 1
fi

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3.8 or later:"
    echo "  sudo apt-get update"
    echo "  sudo apt-get install python3 python3-pip python3-venv"
    exit 1
fi

# Get Python version
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "Found Python $PYTHON_VERSION"

# Check Python version (needs 3.8+)
REQUIRED_VERSION="3.8"
if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "Error: Python 3.8 or later is required."
    exit 1
fi

# Install system dependencies
echo ""
echo "Installing system dependencies..."
echo "You may be prompted for your password."

if command -v apt-get &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y \
        python3-pip \
        python3-venv \
        python3-dev \
        libgit2-dev \
        pkg-config \
        build-essential \
        libdbus-1-3 \
        libxkbcommon-x11-0 \
        libxcb-icccm4 \
        libxcb-image0 \
        libxcb-keysyms1 \
        libxcb-randr0 \
        libxcb-render-util0 \
        libxcb-xinerama0 \
        libxcb-xfixes0 \
        qt6-base-dev \
        libqt6gui6 \
        libqt6widgets6 \
        libqt6core6
elif command -v dnf &> /dev/null; then
    sudo dnf install -y \
        python3-pip \
        python3-devel \
        libgit2-devel \
        pkg-config \
        gcc \
        gcc-c++ \
        make \
        qt6-qtbase \
        qt6-qtbase-gui
else
    echo "Warning: Could not detect package manager. Please install dependencies manually."
fi

# Create virtual environment
echo ""
echo "Creating Python virtual environment..."
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install Python dependencies
echo ""
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Install the application
echo ""
echo "Installing GitHub Desktop..."
pip install -e .

# Create desktop entry
echo ""
echo "Creating desktop entry..."

INSTALL_DIR=$(pwd)
DESKTOP_FILE="$HOME/.local/share/applications/github-desktop.desktop"

mkdir -p "$HOME/.local/share/applications"

cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=GitHub Desktop
Comment=GitHub Desktop for Ubuntu
Exec=$INSTALL_DIR/venv/bin/python3 -m github_desktop.main
Icon=$INSTALL_DIR/github_desktop/resources/icon.png
Terminal=false
Categories=Development;RevisionControl;
Keywords=git;github;version control;
EOF

chmod +x "$DESKTOP_FILE"

# Create launcher script
echo ""
echo "Creating launcher script..."

LAUNCHER="$INSTALL_DIR/github-desktop"

cat > "$LAUNCHER" << EOF
#!/bin/bash
cd "$INSTALL_DIR"
source venv/bin/activate
python3 -m github_desktop.main "\$@"
EOF

chmod +x "$LAUNCHER"

# Update desktop database
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database "$HOME/.local/share/applications"
fi

echo ""
echo "=========================================="
echo "Installation Complete!"
echo "=========================================="
echo ""
echo "You can now:"
echo "  1. Launch from applications menu (search for 'GitHub Desktop')"
echo "  2. Run from terminal: $LAUNCHER"
echo "  3. Or activate venv and run: python3 -m github_desktop.main"
echo ""
echo "For first-time use, you'll need a GitHub Personal Access Token."
echo "Create one at: https://github.com/settings/tokens"
echo "Required scopes: repo, user, workflow"
echo ""
