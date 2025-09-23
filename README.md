<!-- Pytest Coverage Comment:Begin -->
<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/README.md"><img alt="Coverage" src="https://img.shields.io/badge/Coverage-92%25-brightgreen.svg" /></a><details><summary>Coverage Report • </summary><table><tr><th>File</th><th>Stmts</th><th>Miss</th><th>Cover</th><th>Missing</th></tr><tbody><tr><td><b>TOTAL</b></td><td><b>140</b></td><td><b>11</b></td><td><b>92%</b></td><td>&nbsp;</td></tr></tbody></table><i>report-only-changed-files is enabled. No files were changed during this commit :)</i></details>
<!-- Pytest Coverage Comment:End -->

# AWS Black Belt MCP Server

A Model Context Protocol (MCP) server that provides search functionality for AWS Black Belt Online Seminars.

## Key Features

- **Seminar Search**: Search AWS Black Belt Online Seminars by keywords

### Tools

1. `search_seminars`: Search AWS Black Belt Online Seminars by keywords

### Current Information Sources

- AWS Black Belt Online Seminars
- PDF materials
- YouTube videos
- Technical category information

## Prerequisites

Python 3.10 or higher is required.

## Configuration

### [Amazon Q Developer CLI](https://github.com/aws/amazon-q-developer-cli)

For use with Amazon Q Developer CLI, add the following configuration to your MCP settings file:

- **Workspace-level configuration**: `.aws/amazonq/cli-agents/default.json`
- **User-level configuration**: `~/.aws/amazonq/cli-agents/default.json`

```json
{
  "mcpServers": {
    "aws-blackbelt-mcp-server": {
      "command": "uvx",
      "args": ["aws-blackbelt-mcp-server==0.1.0rc1"]
    }
  },
  "tools": [
    // .. other existing tools
    "@awslabs.aws-documentation-mcp-server"
  ],
}
```

## Basic Usage

Example:

- "Find AWS Black Belt seminars about machine learning"
