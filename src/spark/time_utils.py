"""Shared time utilities for cache key generation."""

from datetime import datetime
from typing import Optional


def sanitize_timestamp_for_filename(timestamp: Optional[datetime]) -> str:
    """Convert datetime to Windows-safe filename string.

    ISO format timestamps contain colons which are invalid in Windows filenames.
    Also normalizes timestamps by removing microseconds to ensure consistent cache keys.
    This converts timestamps like '2026-01-05T03:22:48.123456+00:00' to '2026-01-05T03-22-48+00-00'.

    Args:
        timestamp: Datetime object to convert

    Returns:
        Windows-safe timestamp string without microseconds
    """
    if not timestamp:
        return "unknown"

    timestamp_no_micro = timestamp.replace(microsecond=0)
    iso_str = timestamp_no_micro.isoformat()
    return iso_str.replace(":", "-")
