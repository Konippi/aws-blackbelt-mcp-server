import pytest
from fastmcp import Client
from fastmcp.exceptions import ToolError

from aws_blackbelt_mcp_server.server import mcp


@pytest.mark.asyncio
async def test_search_seminars():
    """Test search_seminars tool."""
    async with Client(mcp) as client:
        params = {"query": "", "limit": 1}
        res = await client.call_tool("search_seminars", params)

        assert res.is_error is False

        content = res.structured_content
        assert content is not None and len(content["result"]) == 1


@pytest.mark.asyncio
async def test_return_empty_list_when_no_seminars_exist():
    """Test returnn an empty list when no seminars exist."""
    async with Client(mcp) as client:
        params = {"query": "NO_SEMINARS"}
        res = await client.call_tool("search_seminars", params)

        assert res.is_error is False

        content = res.structured_content
        assert content is not None and len(content["result"]) == 0


@pytest.mark.asyncio
async def test_missing_required_params():
    """Test missing required params."""
    async with Client(mcp) as client:
        params = {}

        with pytest.raises(ToolError) as e:
            await client.call_tool("search_seminars", params)

        assert "Input validation error:" in str(e.value)


@pytest.mark.asyncio
async def test_sort_order_validation_invalid_value():
    """Test sort_order validation with invalid value."""
    async with Client(mcp) as client:
        params = {"query": "lambda", "sort_order": "invalid"}

        with pytest.raises(ToolError) as e:
            await client.call_tool("search_seminars", params)

        assert "Input validation error:" in str(e.value)


@pytest.mark.asyncio
async def test_limit_validation_out_of_range():
    """Test limit validation with out of range values."""
    async with Client(mcp) as client:
        # Test limit too small
        params = {"query": "lambda", "limit": 0}
        with pytest.raises(ToolError) as e:
            await client.call_tool("search_seminars", params)
        assert "Input validation error:" in str(e.value)

        # Test limit too large
        params = {"query": "lambda", "limit": 51}
        with pytest.raises(ToolError) as e:
            await client.call_tool("search_seminars", params)
        assert "Input validation error:" in str(e.value)

        # Test negative limit
        params = {"query": "lambda", "limit": -1}
        with pytest.raises(ToolError) as e:
            await client.call_tool("search_seminars", params)
        assert "Input validation error:" in str(e.value)
