import os
import pytest
import libwyag

def test_repo_init(tmp_path):
    """Test initializing a repository in a temporary directory."""
    repo_dir = tmp_path / "test_repo"
    repo_dir.mkdir()
    
    # Run wyag init inside the temp directory
    libwyag.main(["init", str(repo_dir)])
    
    # Assert git structure exists
    git_dir = repo_dir / ".git"
    assert git_dir.exists()
    assert (git_dir / "objects").is_dir()
    assert (git_dir / "refs" / "heads").is_dir()
    assert (git_dir / "config").is_file()
    assert (git_dir / "HEAD").is_file()

    # Read HEAD file content
    with open(git_dir / "HEAD", "r") as f:
        content = f.read().strip()
    assert content == "ref: refs/heads/master"