"""Path resolution utilities for the AWS Black Belt MCP server."""

from pathlib import Path


def get_project_root() -> Path:
    """Get the project root directory.

    Returns:
        Path: The absolute path to the project root directory.
    """
    return Path(__file__).resolve().parent.parent.parent.parent
