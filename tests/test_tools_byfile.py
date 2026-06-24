"""Tests for the by-file tools."""

from __future__ import annotations

import json
from pathlib import Path

from scc_mcp.models import ResponseFormat
from scc_mcp.tools import byfile
from scc_mcp.tools.byfile import HotspotsInput, SortMetric, TopFilesInput

from .conftest import requires_scc


class _FakeMCP:
    def __init__(self) -> None:
        self.tools: dict[str, object] = {}

    def tool(self, *, name: str, annotations=None):  # noqa: ANN001
        def decorator(fn):  # noqa: ANN001
            self.tools[name] = fn
            return fn

        return decorator


def _registered():
    mcp = _FakeMCP()
    byfile.register(mcp)
    return mcp.tools


def test_byfile_tools_registered() -> None:
    tools = _registered()
    assert set(tools) == {
        "scc_top_files",
        "scc_complexity_hotspots",
        "scc_file_metrics",
    }


@requires_scc
def test_top_files_limit(sample_tree: Path) -> None:
    fn = _registered()["scc_top_files"]
    out = fn(
        TopFilesInput(
            path=str(sample_tree),
            limit=1,
            response_format=ResponseFormat.JSON,
        )
    )
    rows = json.loads(out)
    assert len(rows) == 1


@requires_scc
def test_top_files_sort_complexity(sample_tree: Path) -> None:
    fn = _registered()["scc_top_files"]
    out = fn(
        TopFilesInput(
            path=str(sample_tree),
            sort=SortMetric.COMPLEXITY,
            response_format=ResponseFormat.JSON,
        )
    )
    rows = json.loads(out)
    complexities = [r["Complexity"] for r in rows]
    assert complexities == sorted(complexities, reverse=True)


@requires_scc
def test_hotspots_excludes_zero_by_default(sample_tree: Path) -> None:
    fn = _registered()["scc_complexity_hotspots"]
    out = fn(
        HotspotsInput(path=str(sample_tree), response_format=ResponseFormat.JSON)
    )
    rows = json.loads(out)
    assert all(r["Complexity"] > 0 for r in rows)


@requires_scc
def test_file_metrics_full_records(sample_tree: Path) -> None:
    from scc_mcp.models import SccBaseInput

    fn = _registered()["scc_file_metrics"]
    out = fn(
        SccBaseInput(path=str(sample_tree), response_format=ResponseFormat.JSON)
    )
    records = json.loads(out)
    assert records
    # Full scc records carry fields not present in the compact row projection.
    assert "Filename" in records[0]
    assert "Bytes" in records[0]


@requires_scc
def test_file_metrics_markdown(sample_tree: Path) -> None:
    from scc_mcp.models import SccBaseInput

    fn = _registered()["scc_file_metrics"]
    out = fn(SccBaseInput(path=str(sample_tree)))
    assert "| Location |" in out
