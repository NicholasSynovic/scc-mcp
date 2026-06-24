"""Tests for output formatting helpers."""

from __future__ import annotations

import json

from scc_mcp.format import markdown_table, render
from scc_mcp.models import ResponseFormat


def test_markdown_table_basic() -> None:
    out = markdown_table([{"a": 1, "b": 2}], ["a", "b"])
    lines = out.splitlines()
    assert lines[0] == "| a | b |"
    assert lines[1] == "| --- | --- |"
    assert lines[2] == "| 1 | 2 |"


def test_markdown_table_custom_headers() -> None:
    out = markdown_table([{"a": 1}], ["a"], headers=["Alpha"])
    assert out.splitlines()[0] == "| Alpha |"


def test_markdown_table_empty() -> None:
    assert markdown_table([], ["a"]) == "(no results)"


def test_render_markdown() -> None:
    assert render({"x": 1}, ResponseFormat.MARKDOWN, markdown="hello") == "hello"


def test_render_json() -> None:
    out = render({"x": 1}, ResponseFormat.JSON, markdown="hello")
    assert json.loads(out) == {"x": 1}
