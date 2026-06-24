1. Present a table of the top N files
2. Count lines of code on the current working directory
3. CLOC by extension | code feature

## MCP features

Tools wrap the external `scc` binary (assumed installed and on `PATH`).
All tools are read-only, default to scanning the current working directory, and
return human-readable markdown by default or structured JSON via
`response_format`.

### Implemented tools

1. `scc_count_lines` — summary CLOC (code/comment/blank/lines) per language plus
   totals. [covers requirement #2] ✅
2. `scc_top_files` — table of the top N files sorted by a chosen metric
   (`code`, `complexity`, `lines`, ...). Backed by `--by-file`. [covers requirement #1] ✅
3. `scc_by_extension` — breakdown of CLOC per language/extension. [covers requirement #3] ✅
4. `scc_complexity_hotspots` — files ranked by cyclomatic complexity to surface
   refactor targets (zero-complexity files excluded by default). ✅
5. `scc_cost_estimate` — COCOMO cost / schedule / people estimates from
   `--format json2`, with configurable project type (organic, semi-detached, embedded). ✅
6. `scc_list_languages` — supported languages and their extensions (`--languages`),
   with an optional name filter. ✅
7. `scc_file_metrics` — detailed per-file stats for a single file or filtered subset. ✅

### Dropped

- `scc_run` (raw passthrough escape hatch) — intentionally dropped to keep the
  tool surface tight and safe.

### Cross-cutting requirements (apply to all tools)

- **Path safety**: resolve the target path and only scan paths the process has both
  read and execute access to (`os.access(path, os.R_OK | os.X_OK)`); reject otherwise.
  Default target is the current working directory. (`scc_mcp/runner.py:validate_path`)
- **`scc` presence check**: verify `scc` is on `PATH`; fail with a clear, actionable
  error if it is missing. (`scc_mcp/runner.py:find_scc`)
- **Safe invocation**: call `scc` via `subprocess` with an argument list (never the
  shell), enforce a timeout, and surface non-zero exit codes plus `stderr` clearly.
  (`scc_mcp/runner.py:run_scc`)
- **Structured output**: prefer JSON formats (`json`, `json2`) internally; offer the
  caller a choice between markdown (default) and JSON. (`scc_mcp/format.py:render`)
- **Filtering passthrough**: expose include/exclude extensions and exclude directories
  as validated parameters. (`scc_mcp/models.py:SccBaseInput`)
