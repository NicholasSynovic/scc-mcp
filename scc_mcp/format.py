"""Output rendering helpers: markdown tables with a JSON fallback."""

from __future__ import annotations

import json
from typing import Any, Mapping, Sequence

from .models import ResponseFormat


def markdown_table(
    rows: Sequence[Mapping[str, Any]],
    columns: Sequence[str],
    headers: Sequence[str] | None = None,
) -> str:
    """Render a list of dict rows as a GitHub-flavored markdown table.

    Args:
        rows: row mappings.
        columns: keys to pull from each row, in display order.
        headers: optional column titles; defaults to the column keys.

    Returns:
        A markdown table, or "(no results)" when there are no rows.
    """
    if not rows:
        return "(no results)"

    titles = list(headers) if headers is not None else list(columns)
    lines = [
        "| " + " | ".join(titles) + " |",
        "| " + " | ".join("---" for _ in titles) + " |",
    ]
    for row in rows:
        cells = [str(row.get(col, "")) for col in columns]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def render(
    data: Any,
    fmt: ResponseFormat,
    *,
    markdown: str,
) -> str:
    """Return ``markdown`` or a JSON dump of ``data`` based on ``fmt``.

    Args:
        data: structured data to emit when JSON is requested.
        fmt: the requested response format.
        markdown: pre-rendered markdown to emit when markdown is requested.
    """
    if fmt is ResponseFormat.JSON:
        return json.dumps(data, indent=2)
    return markdown
