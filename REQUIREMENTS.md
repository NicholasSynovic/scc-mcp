1. Present a table of the top N files
2. Count lines of code on the current working directory
3. CLOC by extension | code feature

## Proposed MCP features

Tools wrap the external `scc` binary (assumed installed and on `PATH`).
Workflow tools cover common tasks; one passthrough tool is an escape hatch.

### Workflow tools

1. `scc_count_lines` — summary CLOC (code/comment/blank/total) for a path,
   defaulting to the current working directory. [covers requirement #2]
2. `scc_top_files` — table of the top N files sorted by a chosen metric
   (`code`, `complexity`, `lines`, ...). Backed by `--by-file`. [covers requirement #1]
3. `scc_by_extension` — breakdown of CLOC per language/extension. [covers requirement #3]
4. `scc_complexity_hotspots` — files ranked by cyclomatic complexity to surface
   refactor targets (per-file JSON, sorted by `complexity`).
5. `scc_cost_estimate` — COCOMO cost / schedule / people estimates from
   `--format json2`, with configurable project type (organic, semi-detached, embedded).
6. `scc_list_languages` — supported languages and their extensions (`--languages`),
   useful for choosing include/exclude filters.
7. `scc_file_metrics` — detailed per-file stats for a single file or filtered subset.

### Escape-hatch tool

8. `scc_run` — validated passthrough accepting an argument list plus a target path;
   returns raw `scc` output in the requested `--format`. For advanced or unsupported
   flag combinations.

### Cross-cutting requirements (apply to all tools)

- **Path safety**: resolve the target path and only scan paths the process has both
  read and execute access to (`os.access(path, os.R_OK | os.X_OK)`); reject otherwise.
  Default target is the current working directory.
- **`scc` presence check**: verify `scc` is on `PATH`; fail with a clear, actionable
  error if it is missing (it is an external binary, not a Python dependency).
- **Safe invocation**: call `scc` via `subprocess` with an argument list (never the
  shell), enforce a timeout, and surface non-zero exit codes plus `stderr` clearly.
- **Structured output**: prefer JSON formats (`json`, `json2`) internally; offer the
  caller a choice between a human-readable markdown table and machine-readable JSON.
- **Filtering passthrough**: expose include/exclude extensions, exclude directories,
  sort column, percentage values, and top-N limits as validated parameters.

