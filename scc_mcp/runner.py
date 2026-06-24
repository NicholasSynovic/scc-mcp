"""scc invocation and path-safety helpers.

Owns locating the external ``scc`` binary, validating that a target path is safe
to scan, and running ``scc`` as a subprocess with a timeout. All scc calls use an
argument list (never the shell).
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

DEFAULT_TIMEOUT = 120.0


class SccError(RuntimeError):
    """Raised when scc is missing, a path is unsafe, or a run fails."""


def find_scc() -> str:
    """Return the absolute path to the ``scc`` binary.

    Raises:
        SccError: if ``scc`` is not found on ``PATH``.
    """
    path = shutil.which("scc")
    if path is None:
        raise SccError(
            "The 'scc' binary was not found on PATH. Install it from "
            "https://github.com/boyter/scc and ensure it is on your PATH."
        )
    return path


def validate_path(path: str | None) -> Path:
    """Resolve and validate a target path for scanning.

    Defaults to the current working directory. The path must exist and the
    process must have read and execute access to it.

    Raises:
        SccError: if the path does not exist or lacks read+execute access.
    """
    resolved = Path(path).expanduser().resolve() if path else Path.cwd()

    if not resolved.exists():
        raise SccError(f"Path does not exist: {resolved}")
    if not os.access(resolved, os.R_OK | os.X_OK):
        raise SccError(
            f"Path is not accessible (need read + execute): {resolved}"
        )
    return resolved


def run_scc(
    args: list[str],
    path: str | None = None,
    timeout: float = DEFAULT_TIMEOUT,
) -> str:
    """Run ``scc`` with the given flags against a validated path.

    Args:
        args: scc flags (e.g. ``["--format", "json2"]``). Do not include the
            target path here; it is appended after validation.
        path: target directory/file. Defaults to the current working directory.
        timeout: seconds before the subprocess is killed.

    Returns:
        scc's stdout as text.

    Raises:
        SccError: if scc is missing, the path is unsafe, the run times out, or
            scc exits non-zero.
    """
    scc = find_scc()
    target = validate_path(path)
    cmd = [scc, *args, str(target)]

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise SccError(f"scc timed out after {timeout}s: {' '.join(cmd)}") from exc

    if proc.returncode != 0:
        stderr = proc.stderr.strip() or "(no stderr)"
        raise SccError(
            f"scc exited with status {proc.returncode}: {stderr}"
        )
    return proc.stdout


def run_scc_no_path(
    args: list[str],
    timeout: float = DEFAULT_TIMEOUT,
) -> str:
    """Run ``scc`` with flags that take no target path (e.g. ``--languages``).

    Raises:
        SccError: if scc is missing, times out, or exits non-zero.
    """
    scc = find_scc()
    cmd = [scc, *args]

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise SccError(f"scc timed out after {timeout}s: {' '.join(cmd)}") from exc

    if proc.returncode != 0:
        stderr = proc.stderr.strip() or "(no stderr)"
        raise SccError(f"scc exited with status {proc.returncode}: {stderr}")
    return proc.stdout


def run_scc_json(
    args: list[str],
    path: str | None = None,
    timeout: float = DEFAULT_TIMEOUT,
) -> Any:
    """Run scc and parse its stdout as JSON.

    Raises:
        SccError: on the same conditions as :func:`run_scc`, or if the output is
            not valid JSON.
    """
    out = run_scc(args, path=path, timeout=timeout)
    try:
        return json.loads(out)
    except json.JSONDecodeError as exc:
        raise SccError(f"Failed to parse scc JSON output: {exc}") from exc
