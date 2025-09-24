"""Black Belt search tool implementation."""

import re
from typing import Annotated, Any, Dict, List, Literal, Optional

import httpx
from fastmcp import Context, FastMCP
from fastmcp.tools.tool import ToolResult
from mcp.types import TextContent
from pydantic import Field
from youtube_transcript_api import YouTubeTranscriptApi

from aws_blackbelt_mcp_server.config import env

AWS_API_BASE_URL = "https://aws.amazon.com/api"
YOUTUBE_REGEX = r'href="(https://youtu\.be/[^"]+)"'

SEMINAR_TAG_NAMESPACE_ID = "GLOBAL#aws-tech-category"
SEMINAR_DIRECTORY_ID = "events-cards-interactive-event-content-japan"
SEMINAR_LOCALE = "ja_JP"
SEMINAR_QUERY_OPERATOR = "AND"
SEMINAR_SORT_BY = "item.additionalFields.publishedDate"


def register_tools(mcp: FastMCP) -> None:
    """Register tools."""
    mcp.tool()(search_seminars)
    mcp.tool()(get_seminar_transcript)


def _extract_categories_from_tags(tags: List[Dict[str, Any]]) -> List[str]:
    """Extract AWS tech categories from tags."""
    categories = []

    for tag in tags:
        if tag.get("tagNamespaceId") == SEMINAR_TAG_NAMESPACE_ID:
            tag_name = tag.get("name")
            if tag_name and tag_name not in categories:
                categories.append(tag_name)

    return categories


def _extract_youtube_url(body: str) -> Optional[str]:
    """Extract YouTube URL from body text and normalize to standard format."""
    if not body or "youtu.be" not in body:
        return None

    match = re.search(YOUTUBE_REGEX, body)
    if match:
        return match.group(1)

    return None


async def search_seminars(
    ctx: Context,
    query: Annotated[
        str,
        Field(description="Search keyword"),
    ],
    sort_order: Annotated[
        Literal["asc", "desc"],
        Field(description="Sort order", default="desc"),
    ],
    limit: Annotated[
        int,
        Field(description="Max results", default=10, ge=1, le=50),
    ],
) -> ToolResult:
    """Search AWS Black Belt seminars by keyword.

    Args:
        ctx: Context to access MCP features
        query: Search keyword (e.g., "machine learning", "lambda", "s3")
        sort_order: Sort order by published date - "desc" (newest first) or "asc" (oldest first)
        limit: Maximum number of results to return (default: 10, max: 50)

    Returns:
        List of seminar information including title, date, PDF and YouTube links
    """
    params = {
        "item.directoryId": SEMINAR_DIRECTORY_ID,
        "item.locale": SEMINAR_LOCALE,
        "q": query,
        "q_operator": SEMINAR_QUERY_OPERATOR,
        "sort_by": SEMINAR_SORT_BY,
        "sort_order": sort_order,
        "size": limit,
    }

    try:
        await ctx.info(f"Searching Black Belt seminars with query: {query}")

        async with httpx.AsyncClient(base_url=AWS_API_BASE_URL, timeout=env.api_timeout) as client:
            response = await client.get("dirs/items/search", params=params)
            response.raise_for_status()
            data = response.json()

            items = data.get("items", [])

            results = []
            for item_data in items:
                item = item_data.get("item", {})
                additional_fields = item.get("additionalFields", {})
                tags = item_data.get("tags", [])

                categories = _extract_categories_from_tags(tags)
                body = additional_fields.get("body", "")
                youtube_url = _extract_youtube_url(body)

                result = {
                    "id": item.get("name", ""),
                    "title": additional_fields.get("title", ""),
                    "published_date": additional_fields.get("date", ""),
                    "categories": categories,
                    "pdf_url": additional_fields.get("ctaLink", ""),
                    "youtube_url": youtube_url,
                }
                results.append(result)

            await ctx.info(f"Found {len(results)} seminars")

            return ToolResult(
                content=TextContent(type="text", text=f"Found {len(results)} seminars related to {query}"),
                structured_content={"result": results},
            )

    except Exception as e:
        await ctx.error(f"Search failed: {e}")

        return ToolResult(
            content=TextContent(type="text", text=f"Search failed: {e}"),
            structured_content={"result": []},
        )


def _extract_youtube_id_from_url(url: Optional[str]) -> Optional[str]:
    """Extract YouTube video ID from URL."""
    if not url:
        return None

    if "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]

    return None


async def get_seminar_transcript(
    ctx: Context,
    youtube_url: Annotated[
        str,
        Field(description="YouTube video URL"),
    ],
    language: Annotated[
        str,
        Field(description="Language code for transcript (e.g., 'ja', 'en')", default="ja"),
    ],
) -> ToolResult:
    """Get transcript from seminar video.

    Args:
        ctx: Context to access MCP features
        youtube_url: YouTube video URL
        language: Language code for transcript (default: "ja" for Japanese)

    Returns:
        Seminar transcript
    """
    try:
        # Extract video ID from URL
        youtube_id = _extract_youtube_id_from_url(youtube_url)
        if not youtube_id:
            return ToolResult(
                content=TextContent(type="text", text="Invalid YouTube URL or ID"),
                structured_content={"error": "Could not extract video ID from URL"},
            )

        await ctx.info(f"Getting transcript for YouTube video: {youtube_id}")

        api = YouTubeTranscriptApi()

        # Try to get transcript in specified language
        try:
            transcript = api.fetch(youtube_id, languages=[language])
        except Exception:
            return ToolResult(
                content=TextContent(type="text", text="No transcript available"),
                structured_content={"error": "No transcript available for this video"},
            )
        transcript_text = "".join([snippet.text for snippet in transcript.snippets])

        return ToolResult(
            content=TextContent(
                type="text",
                text=f"Retrieved seminar transcript for video {youtube_id} in {language}",
            ),
            structured_content={
                "video_id": transcript.video_id,
                "language": transcript.language_code,
                "transcript": transcript_text,
            },
        )

    except Exception as e:
        await ctx.error(f"Failed to get transcript: {e}")

        return ToolResult(
            content=TextContent(type="text", text=f"Failed to get seminar transcript: {e}"),
            structured_content={"error": str(e)},
        )
