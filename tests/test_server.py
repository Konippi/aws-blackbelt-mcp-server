"""Tests for server.py module."""

from aws_blackbelt_mcp_server import server


def test_main_function(mocker):
    """Test main function starts the server with proper logging and mcp.run call."""
    # Mock logger and mcp
    mock_logger = mocker.patch("aws_blackbelt_mcp_server.server.logger")
    mock_mcp = mocker.patch("aws_blackbelt_mcp_server.server.mcp")

    # Call main function
    server.main()

    # Verify logger was called with expected message
    mock_logger.info.assert_called_with("Starting AWS Black Belt MCP Server...")

    # Verify mcp.run was called once
    mock_mcp.run.assert_called_once()
