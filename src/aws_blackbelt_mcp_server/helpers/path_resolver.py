"""Path resolution utilities for the AWS Black Belt MCP server."""

from pathlib import Path

AWS_CONFIG_DIR = ".aws"
APP_LOG_DIR = "aws-blackbelt-mcp"
LOG_FILE_NAME = "aws-blackbelt-mcp-server.log"


def get_project_root() -> Path:
    """Get the project root directory.

    Returns:
        Path: The absolute path to the project root directory.
    """
    return Path(__file__).resolve().parent.parent.parent.parent


def get_log_directory() -> Path:
    """Get the log directory for AWS Black Belt MCP server.

    Returns:
        Path: The log directory path, creates it if it doesn't exist.
    """
    log_dir = Path.home() / AWS_CONFIG_DIR / APP_LOG_DIR
    log_dir.mkdir(parents=True, exist_ok=True)
    return log_dir


def get_log_file_path() -> Path:
    """Get the log file path for AWS Black Belt MCP server.

    Returns:
        Path: The log file path.
    """
    return get_log_directory() / LOG_FILE_NAME
