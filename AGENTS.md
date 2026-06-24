# AGENTS.md

## What this is
MCP (Model Context Protocol) server that exposes [`boyter/scc`](https://github.com/boyter/scc)
(a code-counting / complexity tool) to an LLM. Python project managed with `uv`.

## Current state
`uv` project (Python 3.14). Dep: `fastmcp` (standalone v2); dev dep: `pytest`.
Server exposes 7 read-only scc tools (see `REQUIREMENTS.md`). Registered as a
local MCP in `opencode.json` via `uv run scc-mcp`.

## Layout
- `scc_mcp/main.py` — `FastMCP` instance + `main()`; imports each tool module and
  calls its `register(mcp)`.
- `scc_mcp/runner.py` — scc location, path safety, subprocess invocation
  (`find_scc`, `validate_path`, `run_scc`, `run_scc_json`, `run_scc_no_path`).
- `scc_mcp/models.py` — `ResponseFormat` enum + `SccBaseInput` (path, filters).
- `scc_mcp/format.py` — `markdown_table` + `render` (markdown default, JSON fallback).
- `scc_mcp/tools/{summary,byfile,languages}.py` — tool defs grouped by scc backend
  (json2 / json --by-file / --languages). Each exposes `register(mcp)`.

## Commands
- Install deps: `uv sync`
- Add a dep: `uv add <pkg>` / dev dep: `uv add --dev <pkg>` (don't hand-edit deps)
- Run server (stdio): `uv run scc-mcp`
- Run tests: `uv run pytest`
- Build artifacts: `make build`

## Conventions / gotchas
- Import is `from fastmcp import FastMCP` (standalone v2), NOT the official SDK's
  `from mcp.server.fastmcp import FastMCP`. The two APIs differ; follow fastmcp v2 docs.
- Pydantic input models passed to `@mcp.tool` must be **module-level**, not defined
  inside a closure — FastMCP resolves type hints against module globals and will
  raise `NameError` otherwise.
- `scc` is an external binary, not a Python dependency. Assume it is installed and on
  `PATH` — do NOT install it. Invocations must fail clearly if it is missing.
- Only scan paths with read + execute access (`os.access(p, os.R_OK | os.X_OK)`); default
  to the current working directory.
- Tests that shell out to scc are guarded by the `requires_scc` skip marker in
  `tests/conftest.py`; the `sample_tree` fixture builds a tmp multi-language project.
- Useful `scc` machine-readable output: `--format json2` (project summary + COCOMO),
  `--format json --by-file` (per-file stats incl. complexity), `--languages` (no path).
