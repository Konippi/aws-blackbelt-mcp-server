import tempfile
from pathlib import Path

from src.aws_blackbelt_mcp_server.helpers.path_resolver import (
    get_log_directory,
    get_log_file_path,
    get_project_root,
)


def test_get_project_root() -> None:
    """Test that get_project_root returns the correct project root."""
    result = get_project_root()
    assert (result / "pyproject.toml").exists()


def test_get_log_directory(mocker) -> None:
    """Test that get_log_directory creates and returns the correct directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        mocker.patch("pathlib.Path.home", return_value=Path(temp_dir))
        log_dir = get_log_directory()

        # Check that the directory exists
        assert log_dir.exists()
        assert log_dir.is_dir()

        # Check the directory structure
        expected_path = Path(temp_dir) / ".aws" / "aws-blackbelt-mcp"
        assert log_dir == expected_path


def test_get_log_file_path(mocker) -> None:
    """Test that get_log_file_path returns the correct file path."""
    with tempfile.TemporaryDirectory() as temp_dir:
        mocker.patch("pathlib.Path.home", return_value=Path(temp_dir))
        log_file = get_log_file_path()

        # Check the file path structure
        expected_path = Path(temp_dir) / ".aws" / "aws-blackbelt-mcp" / "aws-blackbelt-mcp-server.log"
        assert log_file == expected_path
