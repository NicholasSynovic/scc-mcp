"""Tests for the scc runner and path-safety layer."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from scc_mcp.runner import (
    SccError,
    find_scc,
    run_scc,
    run_scc_json,
    validate_path,
)

from .conftest import requires_scc


@requires_scc
def test_find_scc_returns_path() -> None:
    assert os.path.basename(find_scc()).startswith("scc")


def test_validate_path_defaults_to_cwd() -> None:
    assert validate_path(None) == Path.cwd()


def test_validate_path_resolves_existing(tmp_path: Path) -> None:
    assert validate_path(str(tmp_path)) == tmp_path.resolve()


def test_validate_path_rejects_missing() -> None:
    with pytest.raises(SccError, match="does not exist"):
        validate_path("/definitely/not/a/real/path/zzz")


def test_validate_path_rejects_inaccessible(tmp_path: Path) -> None:
    locked = tmp_path / "locked"
    locked.mkdir()
    os.chmod(locked, 0o000)
    try:
        # Root bypasses permission checks; skip if running as root.
        if os.access(locked, os.R_OK | os.X_OK):
            pytest.skip("running as root; permission check bypassed")
        with pytest.raises(SccError, match="not accessible"):
            validate_path(str(locked))
    finally:
        os.chmod(locked, 0o755)


@requires_scc
def test_run_scc_returns_text(sample_tree: Path) -> None:
    out = run_scc(["--format", "json2"], path=str(sample_tree))
    assert out.strip().startswith("{")


@requires_scc
def test_run_scc_json_parses(sample_tree: Path) -> None:
    data = run_scc_json(["--format", "json2"], path=str(sample_tree))
    assert "languageSummary" in data
    names = {lang["Name"] for lang in data["languageSummary"]}
    assert {"Go", "Python"} <= names
