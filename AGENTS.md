# AGENTS.md

## What this is
MCP (Model Context Protocol) server that exposes [`boyter/scc`](https://github.com/boyter/scc)
(a code-counting / complexity tool) to an LLM. Python project managed with `uv`.

## Current state
`uv` project (Python 3.14). Dependency: `fastmcp` (standalone FastMCP v2).
Server not implemented yet — `main.py` is the `uv init` placeholder. Planned tools
are listed in `REQUIREMENTS.md`.

## Commands
- Install deps: `uv sync`
- Add a dep: `uv add <pkg>` (do not edit `pyproject.toml` deps by hand)
- Run anything in the venv: `uv run <cmd>` (e.g. `uv run python main.py`)
- Verify framework import: `uv run python -c "from fastmcp import FastMCP"`

## Conventions / gotchas
- Import is `from fastmcp import FastMCP` (standalone v2), NOT the official SDK's
  `from mcp.server.fastmcp import FastMCP`. The two APIs differ; follow fastmcp v2 docs.
- `scc` is an external binary, not a Python dependency. Assume it is installed and on
  `PATH` — do NOT install it. Invocations must fail clearly if it is missing.
- Only scan paths with read + execute access (`os.access(p, os.R_OK | os.X_OK)`); default
  to the current working directory.
- Useful `scc` machine-readable output: `--format json2` (project summary + COCOMO),
  `--format json --by-file` (per-file stats incl. complexity), `--languages`.
