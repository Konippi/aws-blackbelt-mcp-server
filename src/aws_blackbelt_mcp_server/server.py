"""sample module."""

import sys

from fastmcp import FastMCP
from loguru import logger

from aws_blackbelt_mcp_server.core.config import SERVER_LOG_LEVEL

# Disable default handler
logger.remove()
logger.add(sys.stderr, level=SERVER_LOG_LEVEL)


mcp = FastMCP("sample")


@mcp.tool
def hello() -> str:
    """Hello."""
    return "Hello World!"


def main():
    """Main entry point for AWS Black Belt MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
