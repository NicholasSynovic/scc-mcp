"""Tests for the json2-backed summary tools."""

from __future__ import annotations

import json
from pathlib import Path

from scc_mcp.tools import summary

from .conftest import requires_scc


class _FakeMCP:
    """Minimal stand-in that captures registered tool callables by name."""

    def __init__(self) -> None:
        self.tools: dict[str, object] = {}

    def tool(self, *, name: str, annotations=None):  # noqa: ANN001
        def decorator(fn):  # noqa: ANN001
            self.tools[name] = fn
            return fn

        return decorator


def _registered():
    mcp = _FakeMCP()
    summary.register(mcp)
    return mcp.tools


def test_summary_tools_registered() -> None:
    tools = _registered()
    assert set(tools) == {"scc_count_lines", "scc_by_extension", "scc_cost_estimate"}


@requires_scc
def test_count_lines_markdown(sample_tree: Path) -> None:
    from scc_mcp.models import SccBaseInput

    fn = _registered()["scc_count_lines"]
    out = fn(SccBaseInput(path=str(sample_tree)))
    assert "| Language |" in out
    assert "Go" in out and "Python" in out
    assert "TOTAL" in out


@requires_scc
def test_count_lines_json(sample_tree: Path) -> None:
    from scc_mcp.models import SccBaseInput, ResponseFormat

    fn = _registered()["scc_count_lines"]
    out = fn(SccBaseInput(path=str(sample_tree), response_format=ResponseFormat.JSON))
    data = json.loads(out)
    assert "languages" in data and "totals" in data
    assert data["totals"]["Code"] > 0


@requires_scc
def test_by_extension(sample_tree: Path) -> None:
    from scc_mcp.models import SccBaseInput

    fn = _registered()["scc_by_extension"]
    out = fn(SccBaseInput(path=str(sample_tree)))
    assert "Complexity" in out
    assert "Go" in out


@requires_scc
def test_count_lines_include_filter(sample_tree: Path) -> None:
    from scc_mcp.models import SccBaseInput, ResponseFormat

    fn = _registered()["scc_count_lines"]
    out = fn(
        SccBaseInput(
            path=str(sample_tree),
            include_ext=["py"],
            response_format=ResponseFormat.JSON,
        )
    )
    data = json.loads(out)
    names = {lang["Name"] for lang in data["languages"]}
    assert names == {"Python"}


@requires_scc
def test_cost_estimate(sample_tree: Path) -> None:
    from scc_mcp.tools.summary import CostEstimateInput

    fn = _registered()["scc_cost_estimate"]
    out = fn(CostEstimateInput(path=str(sample_tree)))
    assert "COCOMO Estimate" in out
    assert "Estimated cost" in out
