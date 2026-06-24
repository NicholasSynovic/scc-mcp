"""Shared pytest fixtures: a small multi-language sample tree."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

SCC_AVAILABLE = shutil.which("scc") is not None

requires_scc = pytest.mark.skipif(
    not SCC_AVAILABLE, reason="scc binary not on PATH"
)


@pytest.fixture
def sample_tree(tmp_path: Path) -> Path:
    """Create a tiny project tree with a couple of languages and complexity."""
    go = tmp_path / "a.go"
    go.write_text(
        'package main\n'
        'import "fmt"\n'
        'func main() {\n'
        '    if true {\n'
        '        fmt.Println("x")\n'
        '    }\n'
        '}\n'
        '// a comment\n'
    )

    sub = tmp_path / "sub"
    sub.mkdir()
    py = sub / "b.py"
    py.write_text(
        "def f(x):\n"
        "    if x:\n"
        "        return 1\n"
        "    return 0\n"
    )
    return tmp_path
