"""Tests for the list_languages tool."""

from __future__ import annotations

import json

from scc_mcp.models import ResponseFormat
from scc_mcp.tools import languages
from scc_mcp.tools.languages import ListLanguagesInput, parse_languages

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
    languages.register(mcp)
    return mcp.tools


def test_languages_tool_registered() -> None:
    assert set(_registered()) == {"scc_list_languages"}


def test_parse_languages_basic() -> None:
    out = "Go (go)\nPython (py,pyw,pyi)\nC++ (cc,cpp,cxx)\n"
    parsed = parse_languages(out)
    by_name = {lang["name"]: lang["extensions"] for lang in parsed}
    assert by_name["Go"] == ["go"]
    assert by_name["Python"] == ["py", "pyw", "pyi"]
    assert by_name["C++"] == ["cc", "cpp", "cxx"]


def test_parse_languages_ignores_blank_and_malformed() -> None:
    parsed = parse_languages("\nGo (go)\nno parens here\n")
    assert parsed == [{"name": "Go", "extensions": ["go"]}]


@requires_scc
def test_list_languages_filter_json() -> None:
    fn = _registered()["scc_list_languages"]
    out = fn(
        ListLanguagesInput(
            name_filter="python", response_format=ResponseFormat.JSON
        )
    )
    data = json.loads(out)
    assert data
    assert all("python" in lang["name"].lower() for lang in data)
    assert any("py" in lang["extensions"] for lang in data)


@requires_scc
def test_list_languages_markdown() -> None:
    fn = _registered()["scc_list_languages"]
    out = fn(ListLanguagesInput(name_filter="go"))
    assert "| Language |" in out
    assert "Go" in out
