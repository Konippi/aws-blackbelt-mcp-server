"""AWS Black Belt MCP Server."""

import sys

from fastmcp import FastMCP
from loguru import logger

from aws_blackbelt_mcp_server.config import HOST, LOG_RETENTION, LOG_ROTATION, PORT, SERVER_LOG_LEVEL
from aws_blackbelt_mcp_server.helpers.path_resolver import get_log_file_path
from aws_blackbelt_mcp_server.tools import seminars

# Initialize logger
logger.remove()
logger.add(sys.stderr, level=SERVER_LOG_LEVEL)
log_file = get_log_file_path()
logger.add(log_file, rotation=LOG_ROTATION, retention=LOG_RETENTION)

# Initialize MCP server
mcp = FastMCP(
    name="AWS Black Belt MCP Server",
)

# Register tools
tools = [seminars.search_seminars]
for tool in tools:
    mcp.tool(tool)


def main():
    """Main entry point for AWS Black Belt MCP server."""
    mcp.run(
        log_level=SERVER_LOG_LEVEL,
        host=HOST,
        port=PORT,
        stateless_http=True,
    )


if __name__ == "__main__":
    main()
