import subprocess
import sys
import pytest

def test_cli_help():
    # Example: run the CLI with --help and check output
    result = subprocess.run([sys.executable, "-m", "src.main", "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "help" in result.stdout.lower() or "usage" in result.stdout.lower()
