"""Black Belt search tool implementation."""

import re
from typing import Annotated, Any, Dict, List, Literal, Optional

import httpx
from fastmcp.tools.tool import ToolResult
from loguru import logger
from mcp.types import TextContent
from pydantic import Field

from aws_blackbelt_mcp_server.config import env
from aws_blackbelt_mcp_server.server import mcp

AWS_API_BASE_URL = "https://aws.amazon.com/api"
YOUTUBE_REGEX = r'href="(https://youtu\.be/[^"]+)"'

SEMINAR_DIRECTORY_ID = "events-cards-interactive-event-content-japan"
SEMINAR_LOCALE = "ja_JP"
SEMINAR_QUERY_OPERATOR = "AND"
SEMINAR_SORT_BY = "item.additionalFields.publishedDate"


def _extract_categories_from_tags(tags: List[Dict[str, Any]]) -> List[str]:
    """Extract AWS tech categories from tags."""
    categories = []
    for tag in tags:
        if tag.get("tagNamespaceId") == "GLOBAL#aws-tech-category":
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


@mcp.tool()
async def search_seminars(
    query: Annotated[
        str,
        Field(description="Search keyword"),
    ],
    sort_order: Annotated[
        Optional[Literal["asc", "desc"]],
        Field(description="Sort order", default="desc"),
    ],
    limit: Annotated[
        Optional[int],
        Field(description="Max results", default=10, ge=1, le=50),
    ],
) -> ToolResult:
    """Search AWS Black Belt seminars by keyword.

    Args:
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
        logger.info(f"Searching Black Belt seminars with query: {query}")

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

                try:
                    result = {
                        "id": item.get("name", ""),
                        "title": additional_fields.get("title", ""),
                        "published_date": additional_fields.get("date", ""),
                        "categories": categories,
                        "pdf_url": additional_fields.get("ctaLink", ""),
                        "youtube_url": youtube_url,
                    }
                    results.append(result)
                except Exception as item_error:
                    logger.warning(f"Failed to process item {item.get('name', 'unknown')}: {item_error}")
                    continue

            logger.info(f"Found {len(results)} seminars")

            return ToolResult(
                content=TextContent(type="text", text=f"Found {len(results)} seminars related to {query}"),
                structured_content={"result": results},
            )

    except Exception as e:
        logger.error(f"Search failed: {e}")

        return ToolResult(
            content=TextContent(type="text", text=f"Search failed: {e}"),
            structured_content={"result": []},
        )
