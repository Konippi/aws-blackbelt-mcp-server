"""MCP Inspector wrapper script for AWS Black Belt MCP server."""

import subprocess
import sys

from aws_blackbelt_mcp_server.helpers import path_resolver


def run_inspector() -> int:
    """Run the MCP inspector for aws-blackbelt-mcp-server."""
    project_root = path_resolver.get_project_root()
    cmd = ["npx", "@modelcontextprotocol/inspector", "uv", "run", "aws-blackbelt-mcp-server"]

    result = subprocess.run(cmd, cwd=project_root, check=False)
    return result.returncode


def main() -> None:
    """Run MCP Inspector with the server."""
    try:
        exit_code = run_inspector()
        sys.exit(exit_code)

    except FileNotFoundError:
        print("Error: npx not found. Please install Node.js and npm.", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Inspection interrupted by user.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Error running inspector: {e}", file=sys.stderr)
        sys.exit(1)
