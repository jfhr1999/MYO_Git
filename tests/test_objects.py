import os
import libwyag

def test_hash_object_and_cat_file(tmp_path, capsys):
    """Test hashing a file and reading it back with cat-file."""
    # Create test repo
    repo_dir = tmp_path / "repo"
    libwyag.main(["init", str(repo_dir)])

    # Create a test file
    sample_file = tmp_path / "hello.txt"
    sample_file.write_text("Hello, WYAG!")

    # Change current working directory to the repo so wyag finds .git
    cwd = os.getcwd()
    os.chdir(repo_dir)
    try:
        # Hash the object and write it to database
        libwyag.main(["hash-object", "-w", str(sample_file)])
        captured = capsys.readouterr()
        obj_hash = captured.out.strip()

        # Check hash length (40 hex chars for SHA-1)
        assert len(obj_hash) == 40

        # Read the object back
        libwyag.main(["cat-file", "blob", obj_hash])
        captured_cat = capsys.readouterr()
        assert captured_cat.out == "Hello, WYAG!"
    finally:
        os.chdir(cwd)