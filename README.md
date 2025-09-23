[![GitHub](https://img.shields.io/badge/GitHub-Konippi/aws--blackbelt--mcp--server-red?style=flat&logo=github)](https://github.com/Konippi/aws-blackbelt-mcp-server)
[![CI](https://github.com/Konippi/aws-blackbelt-mcp-server/actions/workflows/test.yaml/badge.svg?branch=main)](https://github.com/Konippi/aws-blackbelt-mcp-server/actions/workflows/test.yaml)
[![License](https://img.shields.io/badge/license-Apache--2.0-yellow)](LICENSE)
![PyPI version](https://img.shields.io/pypi/v/aws-blackbelt-mcp-server?color=blue)
![Python versions](https://img.shields.io/badge/python-3.10_|_3.11_|_3.12_|_3.13-blue)

<!-- Pytest Coverage Comment:Begin -->
<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/README.md"><img alt="Coverage" src="https://img.shields.io/badge/Coverage-96%25-brightgreen.svg" /></a><details><summary>Coverage Report </summary><table><tr><th>File</th><th>Stmts</th><th>Miss</th><th>Cover</th><th>Missing</th></tr><tbody><tr><td colspan="5"><b>src/aws_blackbelt_mcp_server</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/config.py">config.py</a></td><td>10</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/server.py">server.py</a></td><td>23</td><td>1</td><td>95%</td><td><a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/server.py#L43">43</a></td></tr><tr><td colspan="5"><b>src/aws_blackbelt_mcp_server/helpers</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/helpers/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/helpers/path_resolver.py">path_resolver.py</a></td><td>12</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td colspan="5"><b>src/aws_blackbelt_mcp_server/tools</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py">seminars.py</a></td><td>59</td><td>7</td><td>88%</td><td><a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L44">44</a>, <a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L112-L114">112&ndash;114</a>, <a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L123-L124">123&ndash;124</a>, <a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L126">126</a></td></tr><tr><td colspan="5"><b>tests</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/test_config.py">test_config.py</a></td><td>25</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/test_server.py">test_server.py</a></td><td>7</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td colspan="5"><b>tests/helpers</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/helpers/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/helpers/test_path_resolver.py">test_path_resolver.py</a></td><td>20</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td colspan="5"><b>tests/integration</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/integration/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/integration/test_search_seminars.py">test_search_seminars.py</a></td><td>49</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td colspan="5"><b>tests/tools</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/tools/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/tools/test_seminars.py">test_seminars.py</a></td><td>19</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td><b>TOTAL</b></td><td><b>224</b></td><td><b>8</b></td><td><b>96%</b></td><td>&nbsp;</td></tr></tbody></table></details>
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
