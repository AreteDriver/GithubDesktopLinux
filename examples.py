#!/usr/bin/env python3
"""
Example script demonstrating GitHub Desktop for Ubuntu API usage.

This script shows how to use the core functionality programmatically.
"""

import os
from pathlib import Path
from github_desktop.core.github_client import GitHubClient
from github_desktop.core.git_operations import GitRepository


def example_github_api():
    """Example: Using GitHub API client."""
    print("=== GitHub API Example ===")
    
    client = GitHubClient()
    
    # Note: In a real application, get token from user input or environment
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("Please set GITHUB_TOKEN environment variable")
        return
    
    # Authenticate
    if client.authenticate(token):
        print("✓ Authentication successful")
        
        # Get user info
        user = client.get_user()
        if user:
            print(f"✓ Logged in as: {user.login}")
            print(f"  Name: {user.name}")
            print(f"  Email: {user.email}")
        
        # Get repositories
        repos = client.get_user_repos()
        print(f"\n✓ Found {len(repos)} repositories:")
        for i, repo in enumerate(repos[:5]):  # Show first 5
            print(f"  {i+1}. {repo.full_name}")
            print(f"     Description: {repo.description or 'No description'}")
            print(f"     Stars: {repo.stargazers_count}")
        
        if len(repos) > 5:
            print(f"  ... and {len(repos) - 5} more")
    else:
        print("✗ Authentication failed")


def example_git_operations():
    """Example: Using Git operations."""
    print("\n=== Git Operations Example ===")
    
    # Create a temporary test repository
    test_repo_path = Path("/tmp/test-repo")
    
    if test_repo_path.exists():
        print(f"Using existing repository at {test_repo_path}")
    else:
        print(f"Creating test repository at {test_repo_path}")
        test_repo_path.mkdir(parents=True, exist_ok=True)
        os.system(f"cd {test_repo_path} && git init")
    
    # Open repository
    repo = GitRepository(str(test_repo_path))
    
    if repo.is_valid:
        print("✓ Repository loaded")
        
        # Get current branch
        branch = repo.get_current_branch()
        print(f"✓ Current branch: {branch or 'No branch (empty repo)'}")
        
        # Get status
        status = repo.get_status()
        print(f"✓ Status: {len(status)} files changed")
        
        # Get branches
        branches = repo.get_branches()
        print(f"✓ Branches: {', '.join(branches) if branches else 'None (empty repo)'}")
        
        # Create a test file
        test_file = test_repo_path / "example.txt"
        if not test_file.exists():
            print("\n✓ Creating test file...")
            test_file.write_text("Hello, GitHub Desktop!\n")
            
            # Stage and commit
            if repo.stage_files(["example.txt"]):
                print("✓ File staged")
                
                commit_sha = repo.commit(
                    "Initial commit with example file",
                    "Example User",
                    "user@example.com"
                )
                if commit_sha:
                    print(f"✓ Committed: {commit_sha[:7]}")
        
        # Get commit history
        commits = repo.get_commit_history(limit=5)
        if commits:
            print(f"\n✓ Recent commits ({len(commits)}):")
            for commit in commits:
                print(f"  {commit['short_sha']} - {commit['message'][:50]}")
                print(f"    by {commit['author']} <{commit['email']}>")
        
        # Get user info
        user_name, user_email = repo.get_user_info()
        print(f"\n✓ Git user: {user_name} <{user_email}>")
    else:
        print("✗ Invalid repository")


def example_clone_repository():
    """Example: Cloning a repository."""
    print("\n=== Clone Repository Example ===")
    
    # Clone a small public repository
    url = "https://github.com/github/hello-world.git"
    path = "/tmp/cloned-repo"
    
    print(f"Cloning {url}...")
    print("(This may take a moment...)")
    
    def progress_callback(stats):
        """Progress callback for clone operation."""
        if stats.total_objects > 0:
            percent = (stats.received_objects / stats.total_objects) * 100
            print(f"Progress: {percent:.1f}% ({stats.received_objects}/{stats.total_objects} objects)")
    
    repo = GitRepository.clone(url, path, progress_callback)
    
    if repo and repo.is_valid:
        print("✓ Clone successful")
        
        branch = repo.get_current_branch()
        print(f"✓ On branch: {branch}")
        
        commits = repo.get_commit_history(limit=3)
        print(f"✓ Latest commits:")
        for commit in commits:
            print(f"  {commit['short_sha']} - {commit['message'][:50]}")
    else:
        print("✗ Clone failed")


def main():
    """Run all examples."""
    print("GitHub Desktop for Ubuntu - API Examples\n")
    
    # Run examples
    example_git_operations()
    
    # Only run GitHub API example if token is available
    if os.getenv('GITHUB_TOKEN'):
        example_github_api()
    else:
        print("\n=== GitHub API Example ===")
        print("Skipped: Set GITHUB_TOKEN environment variable to run")
    
    # Uncomment to test cloning (downloads data)
    # example_clone_repository()
    
    print("\n✓ Examples complete!")
    print("\nTo run the full GUI application, use:")
    print("  python3 -m github_desktop.main")


if __name__ == "__main__":
    main()
