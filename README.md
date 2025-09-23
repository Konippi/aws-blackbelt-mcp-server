<!-- Pytest Coverage Comment:Begin -->
<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/README.md"><img alt="Coverage" src="https://img.shields.io/badge/Coverage-92%25-brightgreen.svg" /></a><details><summary>Coverage Report • </summary><table><tr><th>File</th><th>Stmts</th><th>Miss</th><th>Cover</th><th>Missing</th></tr><tbody><tr><td colspan="5"><b>src/aws_blackbelt_mcp_server</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/config.py">config.py</a></td><td>6</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/server.py">server.py</a></td><td>23</td><td>3</td><td>86%</td><td><a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/server.py#L38-L39">38&ndash;39</a>, <a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/server.py#L43">43</a></td></tr><tr><td colspan="5"><b>src/aws_blackbelt_mcp_server/tools</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py">seminars.py</a></td><td>54</td><td>8</td><td>85%</td><td><a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L29">29</a>, <a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L35">35</a>, <a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L98-L100">98&ndash;100</a>, <a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L105-L107">105&ndash;107</a></td></tr><tr><td><b>TOTAL</b></td><td><b>142</b></td><td><b>11</b></td><td><b>92%</b></td><td>&nbsp;</td></tr></tbody></table></details>
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
      "args": ["aws-blackbelt-mcp-server"],
      "disabled": false,
      "autoApprove": []
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
