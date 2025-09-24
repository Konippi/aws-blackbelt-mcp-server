[![GitHub](https://img.shields.io/badge/GitHub-Konippi/aws--blackbelt--mcp--server-red?style=flat&logo=github)](https://github.com/Konippi/aws-blackbelt-mcp-server)
[![CI](https://github.com/Konippi/aws-blackbelt-mcp-server/actions/workflows/test.yaml/badge.svg?branch=main)](https://github.com/Konippi/aws-blackbelt-mcp-server/actions/workflows/test.yaml)
[![License](https://img.shields.io/badge/license-Apache--2.0-yellow)](LICENSE)
![PyPI version](https://img.shields.io/pypi/v/aws-blackbelt-mcp-server?color=blue)
![Python versions](https://img.shields.io/badge/python-3.10_|_3.11_|_3.12_|_3.13-blue)

<!-- Pytest Coverage Comment:Begin -->
<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/README.md"><img alt="Coverage" src="https://img.shields.io/badge/Coverage-95%25-brightgreen.svg" /></a><details><summary>Coverage Report </summary><table><tr><th>File</th><th>Stmts</th><th>Miss</th><th>Cover</th><th>Missing</th></tr><tbody><tr><td colspan="5"><b>src/aws_blackbelt_mcp_server</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/config.py">config.py</a></td><td>10</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/server.py">server.py</a></td><td>19</td><td>1</td><td>94%</td><td><a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/server.py#L39">39</a></td></tr><tr><td colspan="5"><b>src/aws_blackbelt_mcp_server/helpers</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/helpers/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/helpers/path_resolver.py">path_resolver.py</a></td><td>12</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td colspan="5"><b>src/aws_blackbelt_mcp_server/tools</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py">seminars.py</a></td><td>80</td><td>9</td><td>88%</td><td><a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L53">53</a>, <a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L129-L130">129&ndash;130</a>, <a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L132">132</a>, <a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L191">191</a>, <a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L193">193</a>, <a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L205-L206">205&ndash;206</a>, <a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/src/aws_blackbelt_mcp_server/tools/seminars.py#L208">208</a></td></tr><tr><td colspan="5"><b>tests</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/test_config.py">test_config.py</a></td><td>25</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/test_server.py">test_server.py</a></td><td>7</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td colspan="5"><b>tests/helpers</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/helpers/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/helpers/test_path_resolver.py">test_path_resolver.py</a></td><td>20</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td colspan="5"><b>tests/integration</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/integration/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/integration/test_get_seminar_transcript.py">test_get_seminar_transcript.py</a></td><td>55</td><td>4</td><td>92%</td><td><a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/integration/test_get_seminar_transcript.py#L24-L27">24&ndash;27</a></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/integration/test_search_seminars.py">test_search_seminars.py</a></td><td>49</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td colspan="5"><b>tests/tools</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/tools/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/Konippi/aws-blackbelt-mcp-server/blob/main/tests/tools/test_seminars.py">test_seminars.py</a></td><td>27</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td><b>TOTAL</b></td><td><b>304</b></td><td><b>14</b></td><td><b>95%</b></td><td>&nbsp;</td></tr></tbody></table></details>
<!-- Pytest Coverage Comment:End -->

# AWS Black Belt MCP Server

A Model Context Protocol (MCP) server that provides search functionality for AWS Black Belt Online Seminars.

### Tools

1. `search_seminars`: Search AWS Black Belt Online Seminars by keywords
2. `get_seminar_transcript`: Get transcript from seminar YouTube videos (Supported only in Japanese)

### Current Information Sources

- AWS Black Belt Online Seminars
- PDF materials
- YouTube videos
- Seminar transcripts

## Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

## Configuration

#### [Amazon Q Developer CLI](https://github.com/aws/amazon-q-developer-cli)

For use with Amazon Q Developer CLI, add the following configuration to your MCP settings file:

- **Workspace-level configuration**: `.aws/amazonq/cli-agents/default.json`
- **User-level configuration**: `~/.aws/amazonq/cli-agents/default.json`

```json
{
  "mcpServers": {
    "aws-blackbelt-mcp-server": {
      "command": "uvx",
      "args": ["aws-blackbelt-mcp-server"]
    }
  },
  "tools": [
    // .. other existing tools
    "@awslabs.aws-documentation-mcp-server"
  ],
}
```

## Basic Usage

Examples:

- "Find AWS Black Belt seminars about machine learning"
- "Get transcript from this seminar video: https://youtu.be/vWfTe5MHOIk"
