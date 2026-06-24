"""Per-file tools backed by ``scc --format json --by-file``.

The by-file JSON groups files under each language; these tools flatten that into
a single list of file records and then sort/slice/select as needed.
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import Field

from ..format import markdown_table, render
from ..models import ResponseFormat, SccBaseInput
from ..runner import run_scc_json

# scc -s/--sort accepted columns.
_SORT_COLUMNS = ("files", "name", "lines", "blanks", "code", "comments", "complexity")


class SortMetric(str, Enum):
    """Sortable per-file metric (mirrors scc's --sort columns)."""

    CODE = "code"
    COMPLEXITY = "complexity"
    LINES = "lines"
    COMMENTS = "comments"
    BLANKS = "blanks"
    NAME = "name"


class TopFilesInput(SccBaseInput):
    """Inputs for the top-N files listing."""

    limit: int = Field(
        default=10,
        ge=1,
        le=1000,
        description="Maximum number of files to return.",
    )
    sort: SortMetric = Field(
        default=SortMetric.CODE,
        description="Metric to sort files by (descending).",
    )


class HotspotsInput(SccBaseInput):
    """Inputs for complexity hotspots."""

    limit: int = Field(
        default=10,
        ge=1,
        le=1000,
        description="Maximum number of files to return.",
    )
    include_zero: bool = Field(
        default=False,
        description="Include files with zero complexity.",
    )


def _by_file(params: SccBaseInput, sort: str | None = None) -> list[dict[str, Any]]:
    """Run scc by-file and flatten the per-language groups into one file list."""
    args = ["--format", "json", "--by-file", "--no-cocomo", *params.filter_args()]
    if sort:
        args += ["--sort", sort]
    data = run_scc_json(args, path=params.path)

    files: list[dict[str, Any]] = []
    for language in data:
        for f in language.get("Files", []):
            files.append(f)
    return files


def _file_row(f: dict[str, Any]) -> dict[str, Any]:
    """Project a scc file record into a compact display row."""
    return {
        "Location": f.get("Location", f.get("Filename", "")),
        "Language": f.get("Language", ""),
        "Code": f.get("Code", 0),
        "Comment": f.get("Comment", 0),
        "Blank": f.get("Blank", 0),
        "Lines": f.get("Lines", 0),
        "Complexity": f.get("Complexity", 0),
    }


_ROW_COLUMNS = ["Location", "Language", "Code", "Comment", "Blank", "Lines", "Complexity"]


def register(mcp: Any) -> None:
    """Register the per-file tools on the given FastMCP instance."""

    @mcp.tool(
        name="scc_top_files",
        annotations={
            "title": "Top N Files",
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": False,
        },
    )
    def scc_top_files(params: TopFilesInput) -> str:
        """List the top N files under a path, sorted by a chosen metric.

        Args:
            params (TopFilesInput): path (default CWD), response_format, filters,
                limit (default 10), and sort metric (default 'code').

        Returns:
            str: markdown table (default) or JSON of the top files with
            Code/Comment/Blank/Lines/Complexity.
        """
        files = _by_file(params, sort=params.sort.value)[: params.limit]
        rows = [_file_row(f) for f in files]
        md = markdown_table(rows, _ROW_COLUMNS)
        return render(rows, params.response_format, markdown=md)

    @mcp.tool(
        name="scc_complexity_hotspots",
        annotations={
            "title": "Complexity Hotspots",
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": False,
        },
    )
    def scc_complexity_hotspots(params: HotspotsInput) -> str:
        """Rank files by cyclomatic complexity to surface refactor targets.

        Args:
            params (HotspotsInput): path (default CWD), response_format, filters,
                limit (default 10), and include_zero (default False).

        Returns:
            str: markdown table (default) or JSON of the most complex files.
        """
        files = _by_file(params, sort="complexity")
        if not params.include_zero:
            files = [f for f in files if int(f.get("Complexity", 0)) > 0]
        files = files[: params.limit]
        rows = [_file_row(f) for f in files]
        md = markdown_table(rows, _ROW_COLUMNS)
        return render(rows, params.response_format, markdown=md)

    @mcp.tool(
        name="scc_file_metrics",
        annotations={
            "title": "Per-File Metrics",
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": False,
        },
    )
    def scc_file_metrics(params: SccBaseInput) -> str:
        """Report detailed per-file metrics for a file or filtered subset.

        Args:
            params (SccBaseInput): path (default CWD), response_format, and
                include/exclude filters. Point ``path`` at a single file for that
                file's metrics, or a directory for all matching files.

        Returns:
            str: markdown table (default) or JSON with one row per file. The JSON
            form preserves all scc per-file fields.
        """
        files = _by_file(params)
        rows = [_file_row(f) for f in files]
        md = markdown_table(rows, _ROW_COLUMNS)
        # JSON form returns the full, unprojected scc records.
        return render(files, params.response_format, markdown=md)
