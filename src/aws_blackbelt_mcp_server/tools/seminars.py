"""Black Belt search tool implementation."""

import re
from typing import Any, Dict, List, Literal, Optional

import httpx
from loguru import logger

from aws_blackbelt_mcp_server.config import API_TIMEOUT, AWS_API_BASE_URL

YOUTUBE_REGEX = r'href="(https://youtu\.be/[^"]+)"'


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
    if not body or not ("youtu.be" in body or "youtube.com" in body):
        return None

    match = re.search(YOUTUBE_REGEX, body)
    if match:
        return match.group(1)

    return None


async def search_seminars(
    query: str,
    sort_order: Optional[Literal["asc", "desc"]] = "desc",
    limit: Optional[int] = 10,
) -> List[Dict[str, Any]]:
    """Search AWS Black Belt seminars by keyword.

    Args:
        query: Search keyword (e.g., "machine learning", "lambda", "s3")
        sort_order: Sort order by published date - "desc" (newest first) or "asc" (oldest first)
        limit: Maximum number of results to return (default: 10, max: 50)

    Returns:
        List of seminar information including title, date, PDF and YouTube links
    """
    search_endpoint = "dirs/items/search"

    params = {
        "item.directoryId": "events-cards-interactive-event-content-japan",
        "item.locale": "ja_JP",
        "q": query,
        "q_operator": "AND",
        "sort_by": "item.additionalFields.publishedDate",
        "sort_order": sort_order,
        "size": limit,
    }

    try:
        logger.info(f"Searching Black Belt seminars with query: {query}")
        logger.info(f"Request URL: {AWS_API_BASE_URL}/{search_endpoint}")
        logger.info(f"Request params: {params}")

        async with httpx.AsyncClient(base_url=AWS_API_BASE_URL, timeout=API_TIMEOUT) as client:
            response = await client.get(search_endpoint, params=params)
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
            return results

    except Exception as e:
        logger.error(f"Search failed: {e}")
        return []
