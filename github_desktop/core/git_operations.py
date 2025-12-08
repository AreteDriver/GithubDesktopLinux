"""Git repository operations wrapper."""

import os
from typing import Optional, List, Dict, Tuple
import pygit2
from pathlib import Path


class GitRepository:
    """Wrapper for Git repository operations using pygit2."""
    
    def __init__(self, repo_path: str):
        """
        Initialize Git repository wrapper.
        
        Args:
            repo_path: Path to the git repository
        """
        self.repo_path = Path(repo_path)
        self._repo: Optional[pygit2.Repository] = None
        
        if self.repo_path.exists():
            try:
                self._repo = pygit2.Repository(str(self.repo_path))
            except Exception as e:
                print(f"Failed to open repository: {e}")
    
    @property
    def is_valid(self) -> bool:
        """Check if repository is valid."""
        return self._repo is not None
    
    @staticmethod
    def clone(url: str, path: str, progress_callback=None) -> Optional['GitRepository']:
        """
        Clone a repository.
        
        Args:
            url: Repository URL
            path: Local path to clone to
            progress_callback: Optional callback for progress updates
            
        Returns:
            GitRepository instance or None
        """
        try:
            callbacks = pygit2.RemoteCallbacks()
            if progress_callback:
                callbacks.transfer_progress = progress_callback
            
            pygit2.clone_repository(url, path, callbacks=callbacks)
            return GitRepository(path)
        except Exception as e:
            print(f"Clone failed: {e}")
            return None
    
    def get_status(self) -> Dict[str, int]:
        """
        Get repository status.
        
        Returns:
            Dictionary with file statuses
        """
        if not self._repo:
            return {}
        
        status_dict = {}
        for filepath, flags in self._repo.status().items():
            status_dict[filepath] = flags
        return status_dict
    
    def get_modified_files(self) -> List[str]:
        """Get list of modified files."""
        if not self._repo:
            return []
        
        modified = []
        for filepath, flags in self._repo.status().items():
            if flags != pygit2.GIT_STATUS_CURRENT:
                modified.append(filepath)
        return modified
    
    def get_current_branch(self) -> Optional[str]:
        """Get current branch name."""
        if not self._repo:
            return None
        
        try:
            if self._repo.head_is_unborn:
                return None
            return self._repo.head.shorthand
        except Exception:
            return None
    
    def get_branches(self) -> List[str]:
        """Get list of all branches."""
        if not self._repo:
            return []
        
        branches = []
        for branch in self._repo.branches.local:
            branches.append(branch)
        return branches
    
    def get_remote_branches(self) -> List[str]:
        """Get list of remote branches."""
        if not self._repo:
            return []
        
        branches = []
        for branch in self._repo.branches.remote:
            branches.append(branch)
        return branches
    
    def checkout_branch(self, branch_name: str) -> bool:
        """
        Checkout a branch.
        
        Args:
            branch_name: Name of the branch to checkout
            
        Returns:
            True if successful, False otherwise
        """
        if not self._repo:
            return False
        
        try:
            branch = self._repo.branches.get(branch_name)
            if not branch:
                return False
            
            ref = self._repo.lookup_reference(branch.name)
            self._repo.checkout(ref)
            return True
        except Exception as e:
            print(f"Checkout failed: {e}")
            return False
    
    def create_branch(self, branch_name: str, start_point: Optional[str] = None) -> bool:
        """
        Create a new branch.
        
        Args:
            branch_name: Name of the new branch
            start_point: Starting point (commit, branch, tag)
            
        Returns:
            True if successful, False otherwise
        """
        if not self._repo:
            return False
        
        try:
            if start_point:
                commit = self._repo.revparse_single(start_point)
            else:
                commit = self._repo.head.peel()
            
            self._repo.branches.create(branch_name, commit)
            return True
        except Exception as e:
            print(f"Branch creation failed: {e}")
            return False
    
    def stage_files(self, files: List[str]) -> bool:
        """
        Stage files for commit.
        
        Args:
            files: List of file paths to stage
            
        Returns:
            True if successful, False otherwise
        """
        if not self._repo:
            return False
        
        try:
            index = self._repo.index
            for file in files:
                index.add(file)
            index.write()
            return True
        except Exception as e:
            print(f"Staging failed: {e}")
            return False
    
    def stage_all(self) -> bool:
        """Stage all modified files."""
        if not self._repo:
            return False
        
        try:
            index = self._repo.index
            index.add_all()
            index.write()
            return True
        except Exception as e:
            print(f"Staging all failed: {e}")
            return False
    
    def commit(self, message: str, author_name: str, author_email: str) -> Optional[str]:
        """
        Create a commit.
        
        Args:
            message: Commit message
            author_name: Author name
            author_email: Author email
            
        Returns:
            Commit SHA or None
        """
        if not self._repo:
            return None
        
        try:
            index = self._repo.index
            tree = index.write_tree()
            
            author = pygit2.Signature(author_name, author_email)
            committer = author
            
            parents = []
            if not self._repo.head_is_unborn:
                parents = [self._repo.head.target]
            
            oid = self._repo.create_commit(
                'HEAD',
                author,
                committer,
                message,
                tree,
                parents
            )
            return str(oid)
        except Exception as e:
            print(f"Commit failed: {e}")
            return None
    
    def get_commit_history(self, limit: int = 50) -> List[Dict]:
        """
        Get commit history.
        
        Args:
            limit: Maximum number of commits to retrieve
            
        Returns:
            List of commit information dictionaries
        """
        if not self._repo or self._repo.head_is_unborn:
            return []
        
        commits = []
        try:
            for i, commit in enumerate(self._repo.walk(self._repo.head.target)):
                if i >= limit:
                    break
                
                commits.append({
                    'sha': str(commit.id),
                    'short_sha': str(commit.id)[:7],
                    'message': commit.message.strip(),
                    'author': commit.author.name,
                    'email': commit.author.email,
                    'timestamp': commit.commit_time,
                })
        except Exception as e:
            print(f"Failed to get commit history: {e}")
        
        return commits
    
    def get_diff(self, commit_sha: Optional[str] = None) -> Optional[str]:
        """
        Get diff for uncommitted changes or a specific commit.
        
        Args:
            commit_sha: Optional commit SHA to get diff for
            
        Returns:
            Diff as string or None
        """
        if not self._repo:
            return None
        
        try:
            if commit_sha:
                commit = self._repo.get(commit_sha)
                if len(commit.parents) > 0:
                    diff = self._repo.diff(commit.parents[0], commit)
                else:
                    diff = commit.tree.diff_to_tree()
            else:
                diff = self._repo.diff()
            
            return diff.patch
        except Exception as e:
            print(f"Failed to get diff: {e}")
            return None
    
    def pull(self, remote_name: str = "origin") -> Tuple[bool, str]:
        """
        Pull changes from remote.
        
        Args:
            remote_name: Name of the remote
            
        Returns:
            Tuple of (success, message)
        """
        if not self._repo:
            return False, "Repository not initialized"
        
        try:
            remote = self._repo.remotes[remote_name]
            remote.fetch()
            
            remote_branch_name = f"{remote_name}/{self.get_current_branch()}"
            remote_ref = self._repo.lookup_reference(f"refs/remotes/{remote_branch_name}")
            
            self._repo.merge(remote_ref.target)
            
            if self._repo.index.conflicts:
                return False, "Merge conflicts detected"
            
            # Get user info for merge commit
            user_name, user_email = self.get_user_info()
            
            author = pygit2.Signature(user_name, user_email)
            tree = self._repo.index.write_tree()
            
            self._repo.create_commit(
                'HEAD',
                author,
                author,
                f"Merge branch '{remote_branch_name}'",
                tree,
                [self._repo.head.target, remote_ref.target]
            )
            
            self._repo.state_cleanup()
            return True, "Pull successful"
        except Exception as e:
            return False, f"Pull failed: {e}"
    
    def push(self, remote_name: str = "origin") -> Tuple[bool, str]:
        """
        Push changes to remote.
        
        Args:
            remote_name: Name of the remote
            
        Returns:
            Tuple of (success, message)
        """
        if not self._repo:
            return False, "Repository not initialized"
        
        try:
            remote = self._repo.remotes[remote_name]
            branch = self.get_current_branch()
            
            if not branch:
                return False, "No active branch"
            
            refspec = f"refs/heads/{branch}:refs/heads/{branch}"
            remote.push([refspec])
            
            return True, "Push successful"
        except Exception as e:
            return False, f"Push failed: {e}"
    
    def get_remotes(self) -> List[str]:
        """Get list of remotes."""
        if not self._repo:
            return []
        
        return [remote.name for remote in self._repo.remotes]
    
    def get_remote_url(self, remote_name: str = "origin") -> Optional[str]:
        """Get URL of a remote."""
        if not self._repo:
            return None
        
        try:
            remote = self._repo.remotes[remote_name]
            return remote.url
        except Exception:
            return None
    
    def get_user_info(self) -> Tuple[str, str]:
        """
        Get user name and email from git config.
        
        Returns:
            Tuple of (name, email) with defaults if not configured
        """
        if not self._repo:
            return "GitHub Desktop User", "user@localhost"
        
        try:
            # Try to get from local config first, then global
            config = self._repo.config
            user_name = config.get_string('user.name')
        except Exception:
            user_name = None
        
        try:
            config = self._repo.config
            user_email = config.get_string('user.email')
        except Exception:
            user_email = None
        
        # Fallback to reasonable defaults
        if not user_name:
            user_name = "GitHub Desktop User"
        if not user_email:
            user_email = "user@localhost"
        
        return user_name, user_email
