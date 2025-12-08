"""GitHub API client wrapper."""

import os
from typing import Optional, List, Dict, Any
import keyring
from github import Github, Auth
from github.Repository import Repository
from github.PullRequest import PullRequest


class GitHubClient:
    """Wrapper for GitHub API operations."""
    
    SERVICE_NAME = "github-desktop-ubuntu"
    
    def __init__(self):
        """Initialize the GitHub client."""
        self._client: Optional[Github] = None
        self._token: Optional[str] = None
        
    def authenticate(self, token: str) -> bool:
        """
        Authenticate with GitHub using a personal access token.
        
        Args:
            token: GitHub personal access token
            
        Returns:
            True if authentication successful, False otherwise
        """
        try:
            auth = Auth.Token(token)
            self._client = Github(auth=auth)
            # Test the connection
            user = self._client.get_user()
            user.login  # This will raise an exception if auth fails
            
            # Store token securely
            self._token = token
            keyring.set_password(self.SERVICE_NAME, "github_token", token)
            return True
        except Exception as e:
            print(f"Authentication failed: {e}")
            return False
    
    def load_stored_token(self) -> bool:
        """
        Load previously stored authentication token.
        
        Returns:
            True if token loaded and valid, False otherwise
        """
        try:
            token = keyring.get_password(self.SERVICE_NAME, "github_token")
            if token:
                return self.authenticate(token)
            return False
        except Exception as e:
            print(f"Failed to load stored token: {e}")
            return False
    
    def logout(self):
        """Clear authentication and stored credentials."""
        try:
            keyring.delete_password(self.SERVICE_NAME, "github_token")
        except Exception:
            pass
        self._client = None
        self._token = None
    
    def is_authenticated(self) -> bool:
        """Check if client is authenticated."""
        return self._client is not None
    
    def get_user(self) -> Optional[Any]:
        """Get the authenticated user."""
        if not self._client:
            return None
        try:
            return self._client.get_user()
        except Exception as e:
            print(f"Failed to get user: {e}")
            return None
    
    def get_user_repos(self, affiliation: str = "owner,collaborator") -> List[Repository]:
        """
        Get repositories for the authenticated user.
        
        Args:
            affiliation: Repository affiliation filter
            
        Returns:
            List of repositories
        """
        if not self._client:
            return []
        try:
            user = self._client.get_user()
            repos = user.get_repos(affiliation=affiliation, sort="updated")
            return list(repos)
        except Exception as e:
            print(f"Failed to get repositories: {e}")
            return []
    
    def get_repository(self, full_name: str) -> Optional[Repository]:
        """
        Get a specific repository by full name.
        
        Args:
            full_name: Repository full name (owner/repo)
            
        Returns:
            Repository object or None
        """
        if not self._client:
            return None
        try:
            return self._client.get_repo(full_name)
        except Exception as e:
            print(f"Failed to get repository: {e}")
            return None
    
    def get_pull_requests(self, repo: Repository, state: str = "open") -> List[PullRequest]:
        """
        Get pull requests for a repository.
        
        Args:
            repo: Repository object
            state: PR state filter (open, closed, all)
            
        Returns:
            List of pull requests
        """
        try:
            return list(repo.get_pulls(state=state))
        except Exception as e:
            print(f"Failed to get pull requests: {e}")
            return []
    
    def create_pull_request(
        self,
        repo: Repository,
        title: str,
        body: str,
        head: str,
        base: str = "main"
    ) -> Optional[PullRequest]:
        """
        Create a pull request.
        
        Args:
            repo: Repository object
            title: PR title
            body: PR description
            head: Head branch
            base: Base branch (default: main)
            
        Returns:
            Created pull request or None
        """
        try:
            return repo.create_pull(title=title, body=body, head=head, base=base)
        except Exception as e:
            print(f"Failed to create pull request: {e}")
            return None
