"""The ``scc_list_languages`` tool, backed by ``scc --languages``.

``--languages`` takes no path and prints one ``Name (ext1,ext2,...)`` line per
supported language.
"""

from __future__ import annotations

import re
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from ..format import markdown_table, render
from ..models import ResponseFormat
from ..runner import run_scc_no_path

_LINE_RE = re.compile(r"^(?P<name>.+?)\s+\((?P<exts>.*)\)\s*$")


class ListLanguagesInput(BaseModel):
    """Inputs for listing supported languages."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        extra="forbid",
    )

    response_format: ResponseFormat = Field(
        default=ResponseFormat.MARKDOWN,
        description="'markdown' for human-readable output or 'json' for structured data.",
    )
    name_filter: str = Field(
        default="",
        description="Case-insensitive substring to filter language names (e.g. 'python').",
    )


def parse_languages(output: str) -> list[dict[str, Any]]:
    """Parse ``scc --languages`` output into ``{name, extensions}`` records."""
    languages: list[dict[str, Any]] = []
    for line in output.splitlines():
        line = line.strip()
        if not line:
            continue
        match = _LINE_RE.match(line)
        if not match:
            continue
        exts = [e.strip() for e in match.group("exts").split(",") if e.strip()]
        languages.append({"name": match.group("name").strip(), "extensions": exts})
    return languages


def register(mcp: Any) -> None:
    """Register the list_languages tool on the given FastMCP instance."""

    @mcp.tool(
        name="scc_list_languages",
        annotations={
            "title": "List Supported Languages",
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": False,
        },
    )
    def scc_list_languages(params: ListLanguagesInput) -> str:
        """List the languages scc recognizes and their file extensions.

        Args:
            params (ListLanguagesInput): response_format and an optional
                case-insensitive name_filter substring.

        Returns:
            str: markdown table (default) or JSON list of
            {name, extensions} records.
        """
        languages = parse_languages(run_scc_no_path(["--languages"]))
        if params.name_filter:
            needle = params.name_filter.lower()
            languages = [
                lang for lang in languages if needle in lang["name"].lower()
            ]

        rows = [
            {"Language": lang["name"], "Extensions": ", ".join(lang["extensions"])}
            for lang in languages
        ]
        md = markdown_table(rows, ["Language", "Extensions"])
        return render(languages, params.response_format, markdown=md)
