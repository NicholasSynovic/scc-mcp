# scc-mcp

An [MCP](https://modelcontextprotocol.io) server that exposes
[`boyter/scc`](https://github.com/boyter/scc) — a fast code-counting and
complexity tool — to LLM agents.

It wraps `scc` in a small set of read-only tools so an agent can count lines of
code, find the largest or most complex files, break stats down by language, and
estimate project cost without learning the `scc` CLI.

## Requirements

- [`uv`](https://docs.astral.sh/uv/)
- [`scc`](https://github.com/boyter/scc) installed and on your `PATH`
  (it is an external binary, **not** a Python dependency, and is not installed
  for you). Verify with `scc --version`.

## Install

```sh
uv sync
```

## Run

The server speaks MCP over stdio:

```sh
uv run scc-mcp
```

## Tools

All tools are read-only. They default to scanning the current working directory
and return human-readable markdown, or structured JSON when
`response_format: "json"` is passed. Most accept include/exclude extension and
directory filters.

| Tool | Description |
| --- | --- |
| `scc_count_lines` | CLOC (code/comment/blank/lines) per language, plus totals. |
| `scc_top_files` | Top N files sorted by a metric (`code`, `complexity`, `lines`, ...). |
| `scc_by_extension` | CLOC broken down per language/extension. |
| `scc_complexity_hotspots` | Files ranked by cyclomatic complexity (refactor targets). |
| `scc_cost_estimate` | COCOMO cost / schedule / people estimate. |
| `scc_file_metrics` | Detailed per-file metrics for a file or filtered subset. |
| `scc_list_languages` | Languages scc recognizes and their file extensions. |

## Use with opencode

This repo registers the server as a local MCP in [`opencode.json`](./opencode.json):

```json
{
  "mcp": {
    "scc": {
      "type": "local",
      "command": ["uv", "run", "scc-mcp"],
      "enabled": true
    }
  }
}
```

For other MCP clients, point them at the same `uv run scc-mcp` command (stdio
transport).

## Development

```sh
uv run pytest     # run the test suite
make build        # build sdist + wheel into dist/
```

Tests that shell out to `scc` are skipped automatically when it is not on
`PATH`. See [`AGENTS.md`](./AGENTS.md) for module layout and conventions.
