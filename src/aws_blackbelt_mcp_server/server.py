"""AWS Black Belt MCP Server."""

import sys

from fastmcp import FastMCP
from loguru import logger

from aws_blackbelt_mcp_server.config import env
from aws_blackbelt_mcp_server.helpers.path_resolver import get_log_file_path

# Initialize logger
logger.remove()
logger.add(sys.stderr, level=env.server_log_level)
log_file = get_log_file_path()
logger.add(log_file, rotation=env.log_rotation, retention=env.log_retention)


def register_tools() -> None:
    """Register all tools."""
    from aws_blackbelt_mcp_server.tools import seminars

    seminars.register_tools(mcp)


# Initialize MCP server
mcp = FastMCP(name="AWS Black Belt MCP Server")

# Register tools
register_tools()


def main():
    """Main entry point for AWS Black Belt MCP server."""
    logger.info("Starting AWS Black Belt MCP Server...")
    mcp.run(transport=env.transport)


if __name__ == "__main__":
    main()
