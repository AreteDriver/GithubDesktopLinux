#!/usr/bin/env python3
"""Setup script for GitHub Desktop for Ubuntu."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="github-desktop-ubuntu",
    version="1.0.0",
    author="GitHub Desktop Ubuntu Team",
    description="The best possible version of GitHub for Ubuntu desktop",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AreteDriver/GithubDesktopLinux",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Version Control :: Git",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyQt6>=6.6.0",
        "PyQt6-WebEngine>=6.6.0",
        "pygit2>=1.13.0",
        "PyGithub>=2.1.1",
        "keyring>=24.3.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "github-desktop=github_desktop.main:main",
        ],
    },
)
