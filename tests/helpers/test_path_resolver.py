from src.aws_blackbelt_mcp_server.helpers.path_resolver import get_project_root


def test_get_project_root() -> None:
    """Test that get_project_root returns the correct project root."""
    result = get_project_root()
    assert (result / "pyproject.toml").exists()
