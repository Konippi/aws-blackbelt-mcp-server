import pytest
from fastmcp import Client
from fastmcp.exceptions import ToolError

from aws_blackbelt_mcp_server.server import mcp


@pytest.mark.asyncio
async def test_get_seminar_transcript_with_valid_url():
    """Test get_seminar_transcript tool with valid YouTube URL."""
    async with Client(mcp) as client:
        # Use a known YouTube video URL (Amazon Cognito: https://youtu.be/vWfTe5MHOIk)
        params = {"youtube_url": "https://youtu.be/vWfTe5MHOIk"}

        res = await client.call_tool("get_seminar_transcript", params)
        content = res.structured_content
        assert content is not None

        if res.is_error or "error" in content:
            # Accept country-related errors as valid outcomes
            error_msg = content.get("error", "")
            pytest.skip(f"Skipping test due to potential network issue: {error_msg}")
        else:
            assert "video_id" in content
            assert "language" in content
            assert "transcript" in content
            assert content["video_id"] == "vWfTe5MHOIk"


@pytest.mark.asyncio
async def test_get_seminar_transcript_with_invalid_url():
    """Test get_seminar_transcript tool with invalid YouTube URL."""
    async with Client(mcp) as client:
        params = {"youtube_url": "https://invalid-url.com"}
        res = await client.call_tool("get_seminar_transcript", params)

        assert res.is_error is False  # Tool doesn't raise error, returns error in content
        content = res.structured_content
        assert content is not None
        assert "error" in content
        assert content["error"] == "Could not extract video ID from URL"


@pytest.mark.asyncio
async def test_get_seminar_transcript_with_empty_url():
    """Test get_seminar_transcript tool with empty URL."""
    async with Client(mcp) as client:
        params = {"youtube_url": ""}
        res = await client.call_tool("get_seminar_transcript", params)

        assert res.is_error is False
        content = res.structured_content
        assert content is not None
        assert "error" in content
        assert content["error"] == "Could not extract video ID from URL"


@pytest.mark.asyncio
async def test_missing_required_params():
    """Test missing required params."""
    async with Client(mcp) as client:
        params = {}

        with pytest.raises(ToolError) as e:
            await client.call_tool("get_seminar_transcript", params)

        assert "Input validation error:" in str(e.value)


@pytest.mark.asyncio
async def test_get_seminar_transcript_no_transcript_available():
    """Test get_seminar_transcript when no transcript is available."""
    async with Client(mcp) as client:
        # Use a video ID that likely doesn't have transcripts
        params = {"youtube_url": "https://youtu.be/nonexistent"}
        res = await client.call_tool("get_seminar_transcript", params)

        assert res.is_error is False
        content = res.structured_content
        assert content is not None
        assert "error" in content
        assert "No transcript available" in content["error"]
