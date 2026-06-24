# Create AGENTS.md for scc-mcp repository

**Session ID:** ses_104f2e880ffejUW7EtVwNVx374
**Created:** 6/24/2026, 2:13:19 PM
**Updated:** 6/24/2026, 2:30:18 PM

---

## User

Create or update `AGENTS.md` for this repository.

The goal is a compact instruction file that helps future OpenCode sessions avoid mistakes and ramp up quickly. Every line should answer: "Would an agent likely miss this without help?" If not, leave it out.

User-provided focus or constraints (honor these):


## How to investigate

Read the highest-value sources first:
- `README*`, root manifests, workspace config, lockfiles
- build, test, lint, formatter, typecheck, and codegen config
- CI workflows and pre-commit / task runner config
- existing instruction files (`AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`, `.cursorrules`, `.github/copilot-instructions.md`)
- repo-local OpenCode config such as `opencode.json`

If architecture is still unclear after reading config and docs, inspect a small number of representative code files to find the real entrypoints, package boundaries, and execution flow. Prefer reading the files that explain how the system is wired together over random leaf files.

Prefer executable sources of truth over prose. If docs conflict with config or scripts, trust the executable source and only keep what you can verify.

## What to extract

Look for the highest-signal facts for an agent working in this repo:
- exact developer commands, especially non-obvious ones
- how to run a single test, a single package, or a focused verification step
- required command order when it matters, such as `lint -> typecheck -> test`
- monorepo or multi-package boundaries, ownership of major directories, and the real app/library entrypoints
- framework or toolchain quirks: generated code, migrations, codegen, build artifacts, special env loading, dev servers, infra deploy flow
- repo-specific style or workflow conventions that differ from defaults
- testing quirks: fixtures, integration test prerequisites, snapshot workflows, required services, flaky or expensive suites
- important constraints from existing instruction files worth preserving

Good `AGENTS.md` content is usually hard-earned context that took reading multiple files to infer.

## Questions

Only ask the user questions if the repo cannot answer something important. Use the `question` tool for one short batch at most.

Good questions:
- undocumented team conventions
- branch / PR / release expectations
- missing setup or test prerequisites that are known but not written down

Do not ask about anything the repo already makes clear.

## Writing rules

Include only high-signal, repo-specific guidance such as:
- exact commands and shortcuts the agent would otherwise guess wrong
- architecture notes that are not obvious from filenames
- conventions that differ from language or framework defaults
- setup requirements, environment quirks, and operational gotchas
- references to existing instruction sources that matter

Exclude:
- generic software advice
- long tutorials or exhaustive file trees
- obvious language conventions
- speculative claims or anything you could not verify
- content better stored in another file referenced via `opencode.json` `instructions`

When in doubt, omit.

Prefer short sections and bullets. If the repo is simple, keep the file simple. If the repo is large, summarize the few structural facts that actually change how an agent should work.

If `AGENTS.md` already exists at `/home/nicholas/Documents/projects/scc-mcp`, improve it in place rather than rewriting blindly. Preserve verified useful guidance, delete fluff or stale claims, and reconcile it with the current codebase.

---

## Assistant (Build · Claude Opus 4.8 · 5.3s)

I'll investigate the repository to understand its structure and create a high-value AGENTS.md file.

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/nicholas/Documents/projects/scc-mcp"
}
```

**Output:**
```
<path>/home/nicholas/Documents/projects/scc-mcp</path>
<type>directory</type>
<entries>
.git/
.gitignore
LICENSE
README.md

(4 entries)
</entries>
```

**Tool: glob**

**Input:**
```json
{
  "pattern": "{AGENTS.md,CLAUDE.md,README*,opencode.json,.cursorrules}"
}
```

**Output:**
```
/home/nicholas/Documents/projects/scc-mcp/README.md
```

---

## Assistant (Build · Claude Opus 4.8 · 3.5s)

The directory looks sparse. Let me check more thoroughly including hidden files and all contents.

**Tool: bash**

**Input:**
```json
{
  "command": "ls -la /home/nicholas/Documents/projects/scc-mcp && echo \"---ALL FILES---\" && git -C /home/nicholas/Documents/projects/scc-mcp ls-files",
  "description": "List all files including tracked git files"
}
```

**Output:**
```
total 28
drwxrwxr-x  3 nicholas nicholas 4096 Jun 24 14:11 .
drwxrwxr-x 19 nicholas nicholas 4096 Jun 24 14:11 ..
drwxrwxr-x  8 nicholas nicholas 4096 Jun 24 14:13 .git
-rw-rw-r--  1 nicholas nicholas 4628 Jun 24 14:11 .gitignore
-rw-rw-r--  1 nicholas nicholas 1503 Jun 24 14:11 LICENSE
-rw-rw-r--  1 nicholas nicholas   80 Jun 24 14:11 README.md
---ALL FILES---
.gitignore
LICENSE
README.md

```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/nicholas/Documents/projects/scc-mcp/README.md"
}
```

**Output:**
```
<path>/home/nicholas/Documents/projects/scc-mcp/README.md</path>
<type>file</type>
<content>
1: # scc-mcp
2: A model context protocol that enables LLM interfacing with boyter/scc

(End of file - total 2 lines)
</content>
```

---

## Assistant (Build · Claude Opus 4.8 · 5.2s)

This is essentially an empty repository - just a README, LICENSE, and .gitignore. There's no code, build config, or test setup yet. Let me check the git history and .gitignore to understand intent.

**Tool: bash**

**Input:**
```json
{
  "command": "git -C /home/nicholas/Documents/projects/scc-mcp log --oneline -20 && echo \"---BRANCH---\" && git -C /home/nicholas/Documents/projects/scc-mcp branch -a",
  "description": "Check git history and branches"
}
```

**Output:**
```
61466f9 Initial commit
---BRANCH---
* main                                 remotes/origin/main
  remotes/origin/HEAD -> origin/main

```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/nicholas/Documents/projects/scc-mcp/.gitignore"
}
```

**Output:**
```
<path>/home/nicholas/Documents/projects/scc-mcp/.gitignore</path>
<type>file</type>
<content>
1: # Byte-compiled / optimized / DLL files
2: __pycache__/
3: *.py[codz]
4: *$py.class
5: 
6: # C extensions
7: *.so
8: 
9: # Distribution / packaging
10: .Python
11: build/
12: develop-eggs/
13: dist/
14: downloads/
15: eggs/
16: .eggs/
17: lib/
18: lib64/
19: parts/
20: sdist/
21: var/
22: wheels/
23: share/python-wheels/
24: *.egg-info/
25: .installed.cfg
26: *.egg
27: MANIFEST
28: 
29: # PyInstaller
30: #   Usually these files are written by a python script from a template
31: #   before PyInstaller builds the exe, so as to inject date/other infos into it.
32: *.manifest
33: *.spec
34: 
35: # Installer logs
36: pip-log.txt
37: pip-delete-this-directory.txt
38: 
39: # Unit test / coverage reports
40: htmlcov/
41: .tox/
42: .nox/
43: .coverage
44: .coverage.*
45: .cache
46: nosetests.xml
47: coverage.xml
48: *.cover
49: *.py.cover
50: .hypothesis/
51: .pytest_cache/
52: cover/
53: 
54: # Translations
55: *.mo
56: *.pot
57: 
58: # Django stuff:
59: *.log
60: local_settings.py
61: db.sqlite3
62: db.sqlite3-journal
63: 
64: # Flask stuff:
65: instance/
66: .webassets-cache
67: 
68: # Scrapy stuff:
69: .scrapy
70: 
71: # Sphinx documentation
72: docs/_build/
73: 
74: # PyBuilder
75: .pybuilder/
76: target/
77: 
78: # Jupyter Notebook
79: .ipynb_checkpoints
80: 
81: # IPython
82: profile_default/
83: ipython_config.py
84: 
85: # pyenv
86: #   For a library or package, you might want to ignore these files since the code is
87: #   intended to run in multiple environments; otherwise, check them in:
88: # .python-version
89: 
90: # pipenv
91: #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
92: #   However, in case of collaboration, if having platform-specific dependencies or dependencies
93: #   having no cross-platform support, pipenv may install dependencies that don't work, or not
94: #   install all needed dependencies.
95: # Pipfile.lock
96: 
97: # UV
98: #   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
99: #   This is especially recommended for binary packages to ensure reproducibility, and is more
100: #   commonly ignored for libraries.
101: # uv.lock
102: 
103: # poetry
104: #   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
105: #   This is especially recommended for binary packages to ensure reproducibility, and is more
106: #   commonly ignored for libraries.
107: #   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
108: # poetry.lock
109: # poetry.toml
110: 
111: # pdm
112: #   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
113: #   pdm recommends including project-wide configuration in pdm.toml, but excluding .pdm-python.
114: #   https://pdm-project.org/en/latest/usage/project/#working-with-version-control
115: # pdm.lock
116: # pdm.toml
117: .pdm-python
118: .pdm-build/
119: 
120: # pixi
121: #   Similar to Pipfile.lock, it is generally recommended to include pixi.lock in version control.
122: # pixi.lock
123: #   Pixi creates a virtual environment in the .pixi directory, just like venv module creates one
124: #   in the .venv directory. It is recommended not to include this directory in version control.
125: .pixi
126: 
127: # PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
128: __pypackages__/
129: 
130: # Celery stuff
131: celerybeat-schedule
132: celerybeat.pid
133: 
134: # Redis
135: *.rdb
136: *.aof
137: *.pid
138: 
139: # RabbitMQ
140: mnesia/
141: rabbitmq/
142: rabbitmq-data/
143: 
144: # ActiveMQ
145: activemq-data/
146: 
147: # SageMath parsed files
148: *.sage.py
149: 
150: # Environments
151: .env
152: .envrc
153: .venv
154: env/
155: venv/
156: ENV/
157: env.bak/
158: venv.bak/
159: 
160: # Spyder project settings
161: .spyderproject
162: .spyproject
163: 
164: # Rope project settings
165: .ropeproject
166: 
167: # mkdocs documentation
168: /site
169: 
170: # mypy
171: .mypy_cache/
172: .dmypy.json
173: dmypy.json
174: 
175: # Pyre type checker
176: .pyre/
177: 
178: # pytype static type analyzer
179: .pytype/
180: 
181: # Cython debug symbols
182: cython_debug/
183: 
184: # PyCharm
185: #   JetBrains specific template is maintained in a separate JetBrains.gitignore that can
186: #   be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
187: #   and can be added to the global gitignore or merged into this file.  For a more nuclear
188: #   option (not recommended) you can uncomment the following to ignore the entire idea folder.
189: # .idea/
190: 
191: # Abstra
192: #   Abstra is an AI-powered process automation framework.
193: #   Ignore directories containing user credentials, local state, and settings.
194: #   Learn more at https://abstra.io/docs
195: .abstra/
196: 
197: # Visual Studio Code
198: #   Visual Studio Code specific template is maintained in a separate VisualStudioCode.gitignore 
199: #   that can be found at https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore
200: #   and can be added to the global gitignore or merged into this file. However, if you prefer, 
201: #   you could uncomment the following to ignore the entire vscode folder
202: # .vscode/
203: # Temporary file for partial code execution
204: tempCodeRunnerFile.py
205: 
206: # Ruff stuff:
207: .ruff_cache/
208: 
209: # PyPI configuration file
210: .pypirc
211: 
212: # Marimo
213: marimo/_static/
214: marimo/_lsp/
215: __marimo__/
216: 
217: # Streamlit
218: .streamlit/secrets.toml

(End of file - total 218 lines)
</content>
```

---

## Assistant (Build · Claude Opus 4.8 · 107.5s)

This is a brand-new, essentially empty repository. There's no code yet — just a README stating intent (a Python MCP server wrapping `boyter/scc`), a standard Python `.gitignore`, and an MIT-style LICENSE.

Writing an AGENTS.md here would mean inventing facts that don't exist — there are no commands, no build config, no architecture, no conventions to document. That would violate the "no speculative claims" rule. There's almost nothing an agent could "miss" because there's nothing here.

Let me confirm the intended direction with the user rather than fabricate content.

**Tool: question**

**Input:**
```json
{
  "questions": [
    {
      "header": "Empty repo — AGENTS.md scope",
      "question": "This repo currently has no code — only README.md (\"MCP server wrapping boyter/scc\"), a Python .gitignore, and a LICENSE. There are no commands, build config, or architecture to document yet, so a verified AGENTS.md would be nearly empty. How should I proceed?",
      "options": [
        {
          "label": "Skip for now",
          "description": "Don't create AGENTS.md until there's real code/config to document (recommended given there's nothing verifiable yet)"
        },
        {
          "label": "Write minimal stub",
          "description": "Create a short AGENTS.md capturing only verified facts: it's a Python MCP server wrapping boyter/scc, currently scaffolding-only"
        },
        {
          "label": "Document planned setup",
          "description": "I'll pick a Python toolchain (e.g. uv + ruff + pytest + MCP SDK) and write AGENTS.md for that intended setup"
        }
      ]
    }
  ]
}
```

**Output:**
```
User has answered your questions: "This repo currently has no code — only README.md ("MCP server wrapping boyter/scc"), a Python .gitignore, and a LICENSE. There are no commands, build config, or architecture to document yet, so a verified AGENTS.md would be nearly empty. How should I proceed?"="Write minimal stub". You can now continue with the user's answers in mind.
```

---

## Assistant (Build · Claude Opus 4.8 · 6.5s)

I'll write a minimal stub with only verified facts plus the one non-obvious gotcha worth flagging (the external `scc` binary dependency).

**Tool: write**

**Input:**
```json
{
  "filePath": "/home/nicholas/Documents/projects/scc-mcp/AGENTS.md",
  "content": "# AGENTS.md\n\n## What this is\nMCP (Model Context Protocol) server that exposes [`boyter/scc`](https://github.com/boyter/scc)\n(a code-counting / complexity tool) to an LLM. Python project (per `.gitignore`).\n\n## Current state\nScaffolding only — `README.md`, `LICENSE`, `.gitignore`. No source, build config, tests,\nor dependency manifest exist yet. When adding the first code, also add the toolchain config\n(manifest, lint/test/format) and update this file with the real commands.\n\n## Key constraint\n`scc` is an external binary, not a Python dependency. It must be installed separately and on\n`PATH` for this server to work. Anything invoking `scc` should fail clearly if it's missing.\n"
}
```

**Output:**
```
Wrote file successfully.
```

---

## Assistant (Build · Claude Opus 4.8 · 6.2s)

Done. Created a minimal `AGENTS.md` with only verified facts.

The repo is scaffolding-only (just `README.md`, `LICENSE`, `.gitignore`), so there are no commands, build config, or architecture to document. I kept the file deliberately short and flagged the one non-obvious gotcha worth preserving:

- **What it is**: Python MCP server wrapping `boyter/scc`.
- **Current state**: scaffolding only — with a note to add toolchain config + real commands here once code lands.
- **Key constraint**: `scc` is an external binary on `PATH`, not a pip dependency — the easiest thing for a future agent to get wrong.

When actual source, a manifest, and test/lint config are added, this file should be updated with the exact developer commands.

---

## User

We want to implement a MCP service that wraps arround the `scc` command. Assume that it is already installed. Do not install it. For now leverage `uv` to add the necessary MCP dependencies and explore the `scc --help` command line interface. Propose a list of potential MCP features that we can have. Append these to @REQUIREMENTS.md . Please ask questions 

---

## Assistant (Plan · Claude Opus 4.8 · 3.8s)

I'm in plan mode (read-only), so I'll explore `scc`'s CLI and research MCP setup without making changes, then propose a plan.

**Tool: bash**

**Input:**
```json
{
  "command": "which scc && scc --version",
  "description": "Verify scc is installed and get version"
}
```

**Output:**
```
/home/linuxbrew/.linuxbrew/bin/scc
scc version 3.7.0

```

**Tool: bash**

**Input:**
```json
{
  "command": "uv --version; echo \"---\"; python3 --version",
  "description": "Check uv and python availability"
}
```

**Output:**
```
uv 0.11.18 (Homebrew 2026-06-01 x86_64-unknown-linux-gnu)
---
Python 3.14.5

```

---

## Assistant (Plan · Claude Opus 4.8 · 1.9s)

**Tool: bash**

**Input:**
```json
{
  "command": "scc --help",
  "description": "Inspect scc CLI options"
}
```

**Output:**
```
Sloc, Cloc and Code. Count lines of code in a directory with complexity estimation.
Version 3.7.0
Ben Boyter <ben@boyter.org> + Contributors

Usage:
  scc [flags] [files or directories]

Flags:
      --avg-wage int                       average wage value used for basic COCOMO calculation (default 56286)
      --binary                             disable binary file detection
      --by-file                            display output for every file
  -m, --character                          calculate max and mean characters per line
      --ci                                 enable CI output settings where stdout is ASCII
      --cocomo-project-type string         change COCOMO model type [organic, semi-detached, embedded, "custom,1,1,1,1"] (default "organic")
      --count-as string                    count extension as language [e.g. jsp:htm,chead:"C Header" maps extension jsp to html and chead to C Header]
      --count-ignore                       set to allow .gitignore and .ignore files to be counted
      --currency-symbol string             set currency symbol (default "$")
      --debug                              enable debug output
      --directory-walker-job-workers int   controls the maximum number of workers which will walk the directory tree (default 8)
  -a, --dryness                            calculate the DRYness of the project (implies --uloc)
      --eaf float                          the effort adjustment factor derived from the cost drivers (1.0 if rated nominal) (default 1)
      --exclude-dir strings                directories to exclude (default [.git,.hg,.svn])
  -x, --exclude-ext strings                ignore file extensions (overrides include-ext) [comma separated list: e.g. go,java,js]
  -n, --exclude-file strings               ignore files with matching names (default [package-lock.json,Cargo.lock,yarn.lock,pubspec.lock,Podfile.lock,pnpm-lock.yaml])
      --file-gc-count int                  number of files to parse before turning the GC on (default 10000)
      --file-list-queue-size int           the size of the queue of files found and ready to be read into memory (default 16)
      --file-process-job-workers int       number of goroutine workers that process files collecting stats (default 16)
      --file-summary-job-queue-size int    the size of the queue used to hold processed file statistics before formatting (default 16)
  -f, --format string                      set output format [tabular, wide, json, json2, csv, csv-stream, cloc-yaml, html, html-table, sql, sql-insert, openmetrics] (default "tabular")
      --format-multi string                have multiple format output overriding --format [e.g. tabular:stdout,csv:file.csv,json:file.json]
      --gen                                identify generated files
      --generated-markers strings          string markers in head of generated files (default [do not edit,<auto-generated />])
  -h, --help                               help for scc
  -i, --include-ext strings                limit to file extensions [comma separated list: e.g. go,java,js]
      --include-symlinks                   if set will count symlink files
  -l, --languages                          print supported languages and extensions
      --large-byte-count int               number of bytes a file can contain before being removed from output (default 1000000)
      --large-line-count int               number of lines a file can contain before being removed from output (default 40000)
      --min                                identify minified files
  -z, --min-gen                            identify minified or generated files
      --min-gen-line-length int            number of bytes per average line for file to be considered minified or generated (default 255)
      --no-cocomo                          remove COCOMO calculation output
  -c, --no-complexity                      skip calculation of code complexity
  -d, --no-duplicates                      remove duplicate files from stats and output
      --no-gen                             ignore generated files in output (implies --gen)
      --no-gitignore                       disables .gitignore file logic
      --no-gitmodule                       disables .gitmodules file logic
      --no-hborder                         remove horizontal borders between sections
      --no-ignore                          disables .ignore file logic
      --no-large                           ignore files over certain byte and line size set by large-line-count and large-byte-count
      --no-min                             ignore minified files in output (implies --min)
      --no-min-gen                         ignore minified or generated files in output (implies --min-gen)
      --no-scc-ignore                      disables .sccignore file logic
      --no-size                            remove size calculation output
  -M, --not-match stringArray              ignore files and directories matching regular expression
  -o, --output string                      output filename (default stdout)
      --overhead float                     set the overhead multiplier for corporate overhead (facilities, equipment, accounting, etc.) (default 2.4)
  -p, --percent                            include percentage values in output
      --remap-all string                   inspect every file and remap by checking for a string and remapping the language [e.g. "-*- C++ -*-":"C Header"]
      --remap-unknown string               inspect files of unknown type and remap by checking for a string and remapping the language [e.g. "-*- C++ -*-":"C Header"]
      --size-unit string                   set size unit [si, binary, mixed, xkcd-kb, xkcd-kelly, xkcd-imaginary, xkcd-intel, xkcd-drive, xkcd-bakers] (default "si")
      --sloccount-format                   print a more SLOCCount like COCOMO calculation
  -s, --sort string                        column to sort by [files, name, lines, blanks, code, comments, complexity] (default "files")
      --sql-project string                 use supplied name as the project identifier for the current run. Only valid with the --format sql or sql-insert option
  -t, --trace                              enable trace output (not recommended when processing multiple files)
  -u, --uloc                               calculate the number of unique lines of code (ULOC) for the project
  -v, --verbose                            verbose output
      --version                            version for scc
  -w, --wide                               wider output with additional statistics (implies --complexity)

```

---

## Assistant (Plan · Claude Opus 4.8 · 3.0s)

`scc` is v3.7.0 and on PATH. Now let me research the current MCP Python SDK / FastMCP setup so my proposal uses correct, current dependency info.

**Tool: skill**

**Input:**
```json
{
  "name": "mcp-builder"
}
```

**Output:**
```
<skill_content name="mcp-builder">
# Skill: mcp-builder

# MCP Server Development Guide

## Overview

Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. The quality of an MCP server is measured by how well it enables LLMs to accomplish real-world tasks.

---

# Process

## 🚀 High-Level Workflow

Creating a high-quality MCP server involves four main phases:

### Phase 1: Deep Research and Planning

#### 1.1 Understand Modern MCP Design

**API Coverage vs. Workflow Tools:**
Balance comprehensive API endpoint coverage with specialized workflow tools. Workflow tools can be more convenient for specific tasks, while comprehensive coverage gives agents flexibility to compose operations. Performance varies by client—some clients benefit from code execution that combines basic tools, while others work better with higher-level workflows. When uncertain, prioritize comprehensive API coverage.

**Tool Naming and Discoverability:**
Clear, descriptive tool names help agents find the right tools quickly. Use consistent prefixes (e.g., `github_create_issue`, `github_list_repos`) and action-oriented naming.

**Context Management:**
Agents benefit from concise tool descriptions and the ability to filter/paginate results. Design tools that return focused, relevant data. Some clients support code execution which can help agents filter and process data efficiently.

**Actionable Error Messages:**
Error messages should guide agents toward solutions with specific suggestions and next steps.

#### 1.2 Study MCP Protocol Documentation

**Navigate the MCP specification:**

Start with the sitemap to find relevant pages: `https://modelcontextprotocol.io/sitemap.xml`

Then fetch specific pages with `.md` suffix for markdown format (e.g., `https://modelcontextprotocol.io/specification/draft.md`).

Key pages to review:
- Specification overview and architecture
- Transport mechanisms (streamable HTTP, stdio)
- Tool, resource, and prompt definitions

#### 1.3 Study Framework Documentation

**Recommended stack:**
- **Language**: TypeScript (high-quality SDK support and good compatibility in many execution environments e.g. MCPB. Plus AI models are good at generating TypeScript code, benefiting from its broad usage, static typing and good linting tools)
- **Transport**: Streamable HTTP for remote servers, using stateless JSON (simpler to scale and maintain, as opposed to stateful sessions and streaming responses). stdio for local servers.

**Load framework documentation:**

- **MCP Best Practices**: [📋 View Best Practices](./reference/mcp_best_practices.md) - Core guidelines

**For TypeScript (recommended):**
- **TypeScript SDK**: Use WebFetch to load `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
- [⚡ TypeScript Guide](./reference/node_mcp_server.md) - TypeScript patterns and examples

**For Python:**
- **Python SDK**: Use WebFetch to load `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- [🐍 Python Guide](./reference/python_mcp_server.md) - Python patterns and examples

#### 1.4 Plan Your Implementation

**Understand the API:**
Review the service's API documentation to identify key endpoints, authentication requirements, and data models. Use web search and WebFetch as needed.

**Tool Selection:**
Prioritize comprehensive API coverage. List endpoints to implement, starting with the most common operations.

---

### Phase 2: Implementation

#### 2.1 Set Up Project Structure

See language-specific guides for project setup:
- [⚡ TypeScript Guide](./reference/node_mcp_server.md) - Project structure, package.json, tsconfig.json
- [🐍 Python Guide](./reference/python_mcp_server.md) - Module organization, dependencies

#### 2.2 Implement Core Infrastructure

Create shared utilities:
- API client with authentication
- Error handling helpers
- Response formatting (JSON/Markdown)
- Pagination support

#### 2.3 Implement Tools

For each tool:

**Input Schema:**
- Use Zod (TypeScript) or Pydantic (Python)
- Include constraints and clear descriptions
- Add examples in field descriptions

**Output Schema:**
- Define `outputSchema` where possible for structured data
- Use `structuredContent` in tool responses (TypeScript SDK feature)
- Helps clients understand and process tool outputs

**Tool Description:**
- Concise summary of functionality
- Parameter descriptions
- Return type schema

**Implementation:**
- Async/await for I/O operations
- Proper error handling with actionable messages
- Support pagination where applicable
- Return both text content and structured data when using modern SDKs

**Annotations:**
- `readOnlyHint`: true/false
- `destructiveHint`: true/false
- `idempotentHint`: true/false
- `openWorldHint`: true/false

---

### Phase 3: Review and Test

#### 3.1 Code Quality

Review for:
- No duplicated code (DRY principle)
- Consistent error handling
- Full type coverage
- Clear tool descriptions

#### 3.2 Build and Test

**TypeScript:**
- Run `npm run build` to verify compilation
- Test with MCP Inspector: `npx @modelcontextprotocol/inspector`

**Python:**
- Verify syntax: `python -m py_compile your_server.py`
- Test with MCP Inspector

See language-specific guides for detailed testing approaches and quality checklists.

---

### Phase 4: Create Evaluations

After implementing your MCP server, create comprehensive evaluations to test its effectiveness.

**Load [✅ Evaluation Guide](./reference/evaluation.md) for complete evaluation guidelines.**

#### 4.1 Understand Evaluation Purpose

Use evaluations to test whether LLMs can effectively use your MCP server to answer realistic, complex questions.

#### 4.2 Create 10 Evaluation Questions

To create effective evaluations, follow the process outlined in the evaluation guide:

1. **Tool Inspection**: List available tools and understand their capabilities
2. **Content Exploration**: Use READ-ONLY operations to explore available data
3. **Question Generation**: Create 10 complex, realistic questions
4. **Answer Verification**: Solve each question yourself to verify answers

#### 4.3 Evaluation Requirements

Ensure each question is:
- **Independent**: Not dependent on other questions
- **Read-only**: Only non-destructive operations required
- **Complex**: Requiring multiple tool calls and deep exploration
- **Realistic**: Based on real use cases humans would care about
- **Verifiable**: Single, clear answer that can be verified by string comparison
- **Stable**: Answer won't change over time

#### 4.4 Output Format

Create an XML file with this structure:

```xml
<evaluation>
  <qa_pair>
    <question>Find discussions about AI model launches with animal codenames. One model needed a specific safety designation that uses the format ASL-X. What number X was being determined for the model named after a spotted wild cat?</question>
    <answer>3</answer>
  </qa_pair>
<!-- More qa_pairs... -->
</evaluation>
```

---

# Reference Files

## 📚 Documentation Library

Load these resources as needed during development:

### Core MCP Documentation (Load First)
- **MCP Protocol**: Start with sitemap at `https://modelcontextprotocol.io/sitemap.xml`, then fetch specific pages with `.md` suffix
- [📋 MCP Best Practices](./reference/mcp_best_practices.md) - Universal MCP guidelines including:
  - Server and tool naming conventions
  - Response format guidelines (JSON vs Markdown)
  - Pagination best practices
  - Transport selection (streamable HTTP vs stdio)
  - Security and error handling standards

### SDK Documentation (Load During Phase 1/2)
- **Python SDK**: Fetch from `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- **TypeScript SDK**: Fetch from `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`

### Language-Specific Implementation Guides (Load During Phase 2)
- [🐍 Python Implementation Guide](./reference/python_mcp_server.md) - Complete Python/FastMCP guide with:
  - Server initialization patterns
  - Pydantic model examples
  - Tool registration with `@mcp.tool`
  - Complete working examples
  - Quality checklist

- [⚡ TypeScript Implementation Guide](./reference/node_mcp_server.md) - Complete TypeScript guide with:
  - Project structure
  - Zod schema patterns
  - Tool registration with `server.registerTool`
  - Complete working examples
  - Quality checklist

### Evaluation Guide (Load During Phase 4)
- [✅ Evaluation Guide](./reference/evaluation.md) - Complete evaluation creation guide with:
  - Question creation guidelines
  - Answer verification strategies
  - XML format specifications
  - Example questions and answers
  - Running an evaluation with the provided scripts

Base directory for this skill: file:///home/nicholas/.config/opencode/skills/mcp-builder
Relative paths in this skill (e.g., scripts/, reference/) are relative to this base directory.
Note: file list is sampled.

<skill_files>
<file>/home/nicholas/.config/opencode/skills/mcp-builder/LICENSE.txt</file>
<file>/home/nicholas/.config/opencode/skills/mcp-builder/scripts/evaluation.py</file>
<file>/home/nicholas/.config/opencode/skills/mcp-builder/scripts/requirements.txt</file>
<file>/home/nicholas/.config/opencode/skills/mcp-builder/scripts/connections.py</file>
<file>/home/nicholas/.config/opencode/skills/mcp-builder/scripts/example_evaluation.xml</file>
<file>/home/nicholas/.config/opencode/skills/mcp-builder/reference/mcp_best_practices.md</file>
<file>/home/nicholas/.config/opencode/skills/mcp-builder/reference/evaluation.md</file>
<file>/home/nicholas/.config/opencode/skills/mcp-builder/reference/node_mcp_server.md</file>
<file>/home/nicholas/.config/opencode/skills/mcp-builder/reference/python_mcp_server.md</file>
</skill_files>
</skill_content>
```

---

## Assistant (Plan · Claude Opus 4.8 · 5.1s)

Let me read the Python MCP guide for accurate setup details and check scc's JSON output formats to ground the feature proposals.

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/nicholas/.config/opencode/skills/mcp-builder/reference/python_mcp_server.md"
}
```

**Output:**
```
<path>/home/nicholas/.config/opencode/skills/mcp-builder/reference/python_mcp_server.md</path>
<type>file</type>
<content>
1: # Python MCP Server Implementation Guide
2: 
3: ## Overview
4: 
5: This document provides Python-specific best practices and examples for implementing MCP servers using the MCP Python SDK. It covers server setup, tool registration patterns, input validation with Pydantic, error handling, and complete working examples.
6: 
7: ---
8: 
9: ## Quick Reference
10: 
11: ### Key Imports
12: ```python
13: from mcp.server.fastmcp import FastMCP
14: from pydantic import BaseModel, Field, field_validator, ConfigDict
15: from typing import Optional, List, Dict, Any
16: from enum import Enum
17: import httpx
18: ```
19: 
20: ### Server Initialization
21: ```python
22: mcp = FastMCP("service_mcp")
23: ```
24: 
25: ### Tool Registration Pattern
26: ```python
27: @mcp.tool(name="tool_name", annotations={...})
28: async def tool_function(params: InputModel) -> str:
29:     # Implementation
30:     pass
31: ```
32: 
33: ---
34: 
35: ## MCP Python SDK and FastMCP
36: 
37: The official MCP Python SDK provides FastMCP, a high-level framework for building MCP servers. It provides:
38: - Automatic description and inputSchema generation from function signatures and docstrings
39: - Pydantic model integration for input validation
40: - Decorator-based tool registration with `@mcp.tool`
41: 
42: **For complete SDK documentation, use WebFetch to load:**
43: `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
44: 
45: ## Server Naming Convention
46: 
47: Python MCP servers must follow this naming pattern:
48: - **Format**: `{service}_mcp` (lowercase with underscores)
49: - **Examples**: `github_mcp`, `jira_mcp`, `stripe_mcp`
50: 
51: The name should be:
52: - General (not tied to specific features)
53: - Descriptive of the service/API being integrated
54: - Easy to infer from the task description
55: - Without version numbers or dates
56: 
57: ## Tool Implementation
58: 
59: ### Tool Naming
60: 
61: Use snake_case for tool names (e.g., "search_users", "create_project", "get_channel_info") with clear, action-oriented names.
62: 
63: **Avoid Naming Conflicts**: Include the service context to prevent overlaps:
64: - Use "slack_send_message" instead of just "send_message"
65: - Use "github_create_issue" instead of just "create_issue"
66: - Use "asana_list_tasks" instead of just "list_tasks"
67: 
68: ### Tool Structure with FastMCP
69: 
70: Tools are defined using the `@mcp.tool` decorator with Pydantic models for input validation:
71: 
72: ```python
73: from pydantic import BaseModel, Field, ConfigDict
74: from mcp.server.fastmcp import FastMCP
75: 
76: # Initialize the MCP server
77: mcp = FastMCP("example_mcp")
78: 
79: # Define Pydantic model for input validation
80: class ServiceToolInput(BaseModel):
81:     '''Input model for service tool operation.'''
82:     model_config = ConfigDict(
83:         str_strip_whitespace=True,  # Auto-strip whitespace from strings
84:         validate_assignment=True,    # Validate on assignment
85:         extra='forbid'              # Forbid extra fields
86:     )
87: 
88:     param1: str = Field(..., description="First parameter description (e.g., 'user123', 'project-abc')", min_length=1, max_length=100)
89:     param2: Optional[int] = Field(default=None, description="Optional integer parameter with constraints", ge=0, le=1000)
90:     tags: Optional[List[str]] = Field(default_factory=list, description="List of tags to apply", max_items=10)
91: 
92: @mcp.tool(
93:     name="service_tool_name",
94:     annotations={
95:         "title": "Human-Readable Tool Title",
96:         "readOnlyHint": True,     # Tool does not modify environment
97:         "destructiveHint": False,  # Tool does not perform destructive operations
98:         "idempotentHint": True,    # Repeated calls have no additional effect
99:         "openWorldHint": False     # Tool does not interact with external entities
100:     }
101: )
102: async def service_tool_name(params: ServiceToolInput) -> str:
103:     '''Tool description automatically becomes the 'description' field.
104: 
105:     This tool performs a specific operation on the service. It validates all inputs
106:     using the ServiceToolInput Pydantic model before processing.
107: 
108:     Args:
109:         params (ServiceToolInput): Validated input parameters containing:
110:             - param1 (str): First parameter description
111:             - param2 (Optional[int]): Optional parameter with default
112:             - tags (Optional[List[str]]): List of tags
113: 
114:     Returns:
115:         str: JSON-formatted response containing operation results
116:     '''
117:     # Implementation here
118:     pass
119: ```
120: 
121: ## Pydantic v2 Key Features
122: 
123: - Use `model_config` instead of nested `Config` class
124: - Use `field_validator` instead of deprecated `validator`
125: - Use `model_dump()` instead of deprecated `dict()`
126: - Validators require `@classmethod` decorator
127: - Type hints are required for validator methods
128: 
129: ```python
130: from pydantic import BaseModel, Field, field_validator, ConfigDict
131: 
132: class CreateUserInput(BaseModel):
133:     model_config = ConfigDict(
134:         str_strip_whitespace=True,
135:         validate_assignment=True
136:     )
137: 
138:     name: str = Field(..., description="User's full name", min_length=1, max_length=100)
139:     email: str = Field(..., description="User's email address", pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
140:     age: int = Field(..., description="User's age", ge=0, le=150)
141: 
142:     @field_validator('email')
143:     @classmethod
144:     def validate_email(cls, v: str) -> str:
145:         if not v.strip():
146:             raise ValueError("Email cannot be empty")
147:         return v.lower()
148: ```
149: 
150: ## Response Format Options
151: 
152: Support multiple output formats for flexibility:
153: 
154: ```python
155: from enum import Enum
156: 
157: class ResponseFormat(str, Enum):
158:     '''Output format for tool responses.'''
159:     MARKDOWN = "markdown"
160:     JSON = "json"
161: 
162: class UserSearchInput(BaseModel):
163:     query: str = Field(..., description="Search query")
164:     response_format: ResponseFormat = Field(
165:         default=ResponseFormat.MARKDOWN,
166:         description="Output format: 'markdown' for human-readable or 'json' for machine-readable"
167:     )
168: ```
169: 
170: **Markdown format**:
171: - Use headers, lists, and formatting for clarity
172: - Convert timestamps to human-readable format (e.g., "2024-01-15 10:30:00 UTC" instead of epoch)
173: - Show display names with IDs in parentheses (e.g., "@john.doe (U123456)")
174: - Omit verbose metadata (e.g., show only one profile image URL, not all sizes)
175: - Group related information logically
176: 
177: **JSON format**:
178: - Return complete, structured data suitable for programmatic processing
179: - Include all available fields and metadata
180: - Use consistent field names and types
181: 
182: ## Pagination Implementation
183: 
184: For tools that list resources:
185: 
186: ```python
187: class ListInput(BaseModel):
188:     limit: Optional[int] = Field(default=20, description="Maximum results to return", ge=1, le=100)
189:     offset: Optional[int] = Field(default=0, description="Number of results to skip for pagination", ge=0)
190: 
191: async def list_items(params: ListInput) -> str:
192:     # Make API request with pagination
193:     data = await api_request(limit=params.limit, offset=params.offset)
194: 
195:     # Return pagination info
196:     response = {
197:         "total": data["total"],
198:         "count": len(data["items"]),
199:         "offset": params.offset,
200:         "items": data["items"],
201:         "has_more": data["total"] > params.offset + len(data["items"]),
202:         "next_offset": params.offset + len(data["items"]) if data["total"] > params.offset + len(data["items"]) else None
203:     }
204:     return json.dumps(response, indent=2)
205: ```
206: 
207: ## Error Handling
208: 
209: Provide clear, actionable error messages:
210: 
211: ```python
212: def _handle_api_error(e: Exception) -> str:
213:     '''Consistent error formatting across all tools.'''
214:     if isinstance(e, httpx.HTTPStatusError):
215:         if e.response.status_code == 404:
216:             return "Error: Resource not found. Please check the ID is correct."
217:         elif e.response.status_code == 403:
218:             return "Error: Permission denied. You don't have access to this resource."
219:         elif e.response.status_code == 429:
220:             return "Error: Rate limit exceeded. Please wait before making more requests."
221:         return f"Error: API request failed with status {e.response.status_code}"
222:     elif isinstance(e, httpx.TimeoutException):
223:         return "Error: Request timed out. Please try again."
224:     return f"Error: Unexpected error occurred: {type(e).__name__}"
225: ```
226: 
227: ## Shared Utilities
228: 
229: Extract common functionality into reusable functions:
230: 
231: ```python
232: # Shared API request function
233: async def _make_api_request(endpoint: str, method: str = "GET", **kwargs) -> dict:
234:     '''Reusable function for all API calls.'''
235:     async with httpx.AsyncClient() as client:
236:         response = await client.request(
237:             method,
238:             f"{API_BASE_URL}/{endpoint}",
239:             timeout=30.0,
240:             **kwargs
241:         )
242:         response.raise_for_status()
243:         return response.json()
244: ```
245: 
246: ## Async/Await Best Practices
247: 
248: Always use async/await for network requests and I/O operations:
249: 
250: ```python
251: # Good: Async network request
252: async def fetch_data(resource_id: str) -> dict:
253:     async with httpx.AsyncClient() as client:
254:         response = await client.get(f"{API_URL}/resource/{resource_id}")
255:         response.raise_for_status()
256:         return response.json()
257: 
258: # Bad: Synchronous request
259: def fetch_data(resource_id: str) -> dict:
260:     response = requests.get(f"{API_URL}/resource/{resource_id}")  # Blocks
261:     return response.json()
262: ```
263: 
264: ## Type Hints
265: 
266: Use type hints throughout:
267: 
268: ```python
269: from typing import Optional, List, Dict, Any
270: 
271: async def get_user(user_id: str) -> Dict[str, Any]:
272:     data = await fetch_user(user_id)
273:     return {"id": data["id"], "name": data["name"]}
274: ```
275: 
276: ## Tool Docstrings
277: 
278: Every tool must have comprehensive docstrings with explicit type information:
279: 
280: ```python
281: async def search_users(params: UserSearchInput) -> str:
282:     '''
283:     Search for users in the Example system by name, email, or team.
284: 
285:     This tool searches across all user profiles in the Example platform,
286:     supporting partial matches and various search filters. It does NOT
287:     create or modify users, only searches existing ones.
288: 
289:     Args:
290:         params (UserSearchInput): Validated input parameters containing:
291:             - query (str): Search string to match against names/emails (e.g., "john", "@example.com", "team:marketing")
292:             - limit (Optional[int]): Maximum results to return, between 1-100 (default: 20)
293:             - offset (Optional[int]): Number of results to skip for pagination (default: 0)
294: 
295:     Returns:
296:         str: JSON-formatted string containing search results with the following schema:
297: 
298:         Success response:
299:         {
300:             "total": int,           # Total number of matches found
301:             "count": int,           # Number of results in this response
302:             "offset": int,          # Current pagination offset
303:             "users": [
304:                 {
305:                     "id": str,      # User ID (e.g., "U123456789")
306:                     "name": str,    # Full name (e.g., "John Doe")
307:                     "email": str,   # Email address (e.g., "john@example.com")
308:                     "team": str     # Team name (e.g., "Marketing") - optional
309:                 }
310:             ]
311:         }
312: 
313:         Error response:
314:         "Error: <error message>" or "No users found matching '<query>'"
315: 
316:     Examples:
317:         - Use when: "Find all marketing team members" -> params with query="team:marketing"
318:         - Use when: "Search for John's account" -> params with query="john"
319:         - Don't use when: You need to create a user (use example_create_user instead)
320:         - Don't use when: You have a user ID and need full details (use example_get_user instead)
321: 
322:     Error Handling:
323:         - Input validation errors are handled by Pydantic model
324:         - Returns "Error: Rate limit exceeded" if too many requests (429 status)
325:         - Returns "Error: Invalid API authentication" if API key is invalid (401 status)
326:         - Returns formatted list of results or "No users found matching 'query'"
327:     '''
328: ```
329: 
330: ## Complete Example
331: 
332: See below for a complete Python MCP server example:
333: 
334: ```python
335: #!/usr/bin/env python3
336: '''
337: MCP Server for Example Service.
338: 
339: This server provides tools to interact with Example API, including user search,
340: project management, and data export capabilities.
341: '''
342: 
343: from typing import Optional, List, Dict, Any
344: from enum import Enum
345: import httpx
346: from pydantic import BaseModel, Field, field_validator, ConfigDict
347: from mcp.server.fastmcp import FastMCP
348: 
349: # Initialize the MCP server
350: mcp = FastMCP("example_mcp")
351: 
352: # Constants
353: API_BASE_URL = "https://api.example.com/v1"
354: 
355: # Enums
356: class ResponseFormat(str, Enum):
357:     '''Output format for tool responses.'''
358:     MARKDOWN = "markdown"
359:     JSON = "json"
360: 
361: # Pydantic Models for Input Validation
362: class UserSearchInput(BaseModel):
363:     '''Input model for user search operations.'''
364:     model_config = ConfigDict(
365:         str_strip_whitespace=True,
366:         validate_assignment=True
367:     )
368: 
369:     query: str = Field(..., description="Search string to match against names/emails", min_length=2, max_length=200)
370:     limit: Optional[int] = Field(default=20, description="Maximum results to return", ge=1, le=100)
371:     offset: Optional[int] = Field(default=0, description="Number of results to skip for pagination", ge=0)
372:     response_format: ResponseFormat = Field(default=ResponseFormat.MARKDOWN, description="Output format")
373: 
374:     @field_validator('query')
375:     @classmethod
376:     def validate_query(cls, v: str) -> str:
377:         if not v.strip():
378:             raise ValueError("Query cannot be empty or whitespace only")
379:         return v.strip()
380: 
381: # Shared utility functions
382: async def _make_api_request(endpoint: str, method: str = "GET", **kwargs) -> dict:
383:     '''Reusable function for all API calls.'''
384:     async with httpx.AsyncClient() as client:
385:         response = await client.request(
386:             method,
387:             f"{API_BASE_URL}/{endpoint}",
388:             timeout=30.0,
389:             **kwargs
390:         )
391:         response.raise_for_status()
392:         return response.json()
393: 
394: def _handle_api_error(e: Exception) -> str:
395:     '''Consistent error formatting across all tools.'''
396:     if isinstance(e, httpx.HTTPStatusError):
397:         if e.response.status_code == 404:
398:             return "Error: Resource not found. Please check the ID is correct."
399:         elif e.response.status_code == 403:
400:             return "Error: Permission denied. You don't have access to this resource."
401:         elif e.response.status_code == 429:
402:             return "Error: Rate limit exceeded. Please wait before making more requests."
403:         return f"Error: API request failed with status {e.response.status_code}"
404:     elif isinstance(e, httpx.TimeoutException):
405:         return "Error: Request timed out. Please try again."
406:     return f"Error: Unexpected error occurred: {type(e).__name__}"
407: 
408: # Tool definitions
409: @mcp.tool(
410:     name="example_search_users",
411:     annotations={
412:         "title": "Search Example Users",
413:         "readOnlyHint": True,
414:         "destructiveHint": False,
415:         "idempotentHint": True,
416:         "openWorldHint": True
417:     }
418: )
419: async def example_search_users(params: UserSearchInput) -> str:
420:     '''Search for users in the Example system by name, email, or team.
421: 
422:     [Full docstring as shown above]
423:     '''
424:     try:
425:         # Make API request using validated parameters
426:         data = await _make_api_request(
427:             "users/search",
428:             params={
429:                 "q": params.query,
430:                 "limit": params.limit,
431:                 "offset": params.offset
432:             }
433:         )
434: 
435:         users = data.get("users", [])
436:         total = data.get("total", 0)
437: 
438:         if not users:
439:             return f"No users found matching '{params.query}'"
440: 
441:         # Format response based on requested format
442:         if params.response_format == ResponseFormat.MARKDOWN:
443:             lines = [f"# User Search Results: '{params.query}'", ""]
444:             lines.append(f"Found {total} users (showing {len(users)})")
445:             lines.append("")
446: 
447:             for user in users:
448:                 lines.append(f"## {user['name']} ({user['id']})")
449:                 lines.append(f"- **Email**: {user['email']}")
450:                 if user.get('team'):
451:                     lines.append(f"- **Team**: {user['team']}")
452:                 lines.append("")
453: 
454:             return "\n".join(lines)
455: 
456:         else:
457:             # Machine-readable JSON format
458:             import json
459:             response = {
460:                 "total": total,
461:                 "count": len(users),
462:                 "offset": params.offset,
463:                 "users": users
464:             }
465:             return json.dumps(response, indent=2)
466: 
467:     except Exception as e:
468:         return _handle_api_error(e)
469: 
470: if __name__ == "__main__":
471:     mcp.run()
472: ```
473: 
474: ---
475: 
476: ## Advanced FastMCP Features
477: 
478: ### Context Parameter Injection
479: 
480: FastMCP can automatically inject a `Context` parameter into tools for advanced capabilities like logging, progress reporting, resource reading, and user interaction:
481: 
482: ```python
483: from mcp.server.fastmcp import FastMCP, Context
484: 
485: mcp = FastMCP("example_mcp")
486: 
487: @mcp.tool()
488: async def advanced_search(query: str, ctx: Context) -> str:
489:     '''Advanced tool with context access for logging and progress.'''
490: 
491:     # Report progress for long operations
492:     await ctx.report_progress(0.25, "Starting search...")
493: 
494:     # Log information for debugging
495:     await ctx.log_info("Processing query", {"query": query, "timestamp": datetime.now()})
496: 
497:     # Perform search
498:     results = await search_api(query)
499:     await ctx.report_progress(0.75, "Formatting results...")
500: 
501:     # Access server configuration
502:     server_name = ctx.fastmcp.name
503: 
504:     return format_results(results)
505: 
506: @mcp.tool()
507: async def interactive_tool(resource_id: str, ctx: Context) -> str:
508:     '''Tool that can request additional input from users.'''
509: 
510:     # Request sensitive information when needed
511:     api_key = await ctx.elicit(
512:         prompt="Please provide your API key:",
513:         input_type="password"
514:     )
515: 
516:     # Use the provided key
517:     return await api_call(resource_id, api_key)
518: ```
519: 
520: **Context capabilities:**
521: - `ctx.report_progress(progress, message)` - Report progress for long operations
522: - `ctx.log_info(message, data)` / `ctx.log_error()` / `ctx.log_debug()` - Logging
523: - `ctx.elicit(prompt, input_type)` - Request input from users
524: - `ctx.fastmcp.name` - Access server configuration
525: - `ctx.read_resource(uri)` - Read MCP resources
526: 
527: ### Resource Registration
528: 
529: Expose data as resources for efficient, template-based access:
530: 
531: ```python
532: @mcp.resource("file://documents/{name}")
533: async def get_document(name: str) -> str:
534:     '''Expose documents as MCP resources.
535: 
536:     Resources are useful for static or semi-static data that doesn't
537:     require complex parameters. They use URI templates for flexible access.
538:     '''
539:     document_path = f"./docs/{name}"
540:     with open(document_path, "r") as f:
541:         return f.read()
542: 
543: @mcp.resource("config://settings/{key}")
544: async def get_setting(key: str, ctx: Context) -> str:
545:     '''Expose configuration as resources with context.'''
546:     settings = await load_settings()
547:     return json.dumps(settings.get(key, {}))
548: ```
549: 
550: **When to use Resources vs Tools:**
551: - **Resources**: For data access with simple parameters (URI templates)
552: - **Tools**: For complex operations with validation and business logic
553: 
554: ### Structured Output Types
555: 
556: FastMCP supports multiple return types beyond strings:
557: 
558: ```python
559: from typing import TypedDict
560: from dataclasses import dataclass
561: from pydantic import BaseModel
562: 
563: # TypedDict for structured returns
564: class UserData(TypedDict):
565:     id: str
566:     name: str
567:     email: str
568: 
569: @mcp.tool()
570: async def get_user_typed(user_id: str) -> UserData:
571:     '''Returns structured data - FastMCP handles serialization.'''
572:     return {"id": user_id, "name": "John Doe", "email": "john@example.com"}
573: 
574: # Pydantic models for complex validation
575: class DetailedUser(BaseModel):
576:     id: str
577:     name: str
578:     email: str
579:     created_at: datetime
580:     metadata: Dict[str, Any]
581: 
582: @mcp.tool()
583: async def get_user_detailed(user_id: str) -> DetailedUser:
584:     '''Returns Pydantic model - automatically generates schema.'''
585:     user = await fetch_user(user_id)
586:     return DetailedUser(**user)
587: ```
588: 
589: ### Lifespan Management
590: 
591: Initialize resources that persist across requests:
592: 
593: ```python
594: from contextlib import asynccontextmanager
595: 
596: @asynccontextmanager
597: async def app_lifespan():
598:     '''Manage resources that live for the server's lifetime.'''
599:     # Initialize connections, load config, etc.
600:     db = await connect_to_database()
601:     config = load_configuration()
602: 
603:     # Make available to all tools
604:     yield {"db": db, "config": config}
605: 
606:     # Cleanup on shutdown
607:     await db.close()
608: 
609: mcp = FastMCP("example_mcp", lifespan=app_lifespan)
610: 
611: @mcp.tool()
612: async def query_data(query: str, ctx: Context) -> str:
613:     '''Access lifespan resources through context.'''
614:     db = ctx.request_context.lifespan_state["db"]
615:     results = await db.query(query)
616:     return format_results(results)
617: ```
618: 
619: ### Transport Options
620: 
621: FastMCP supports two main transport mechanisms:
622: 
623: ```python
624: # stdio transport (for local tools) - default
625: if __name__ == "__main__":
626:     mcp.run()
627: 
628: # Streamable HTTP transport (for remote servers)
629: if __name__ == "__main__":
630:     mcp.run(transport="streamable_http", port=8000)
631: ```
632: 
633: **Transport selection:**
634: - **stdio**: Command-line tools, local integrations, subprocess execution
635: - **Streamable HTTP**: Web services, remote access, multiple clients
636: 
637: ---
638: 
639: ## Code Best Practices
640: 
641: ### Code Composability and Reusability
642: 
643: Your implementation MUST prioritize composability and code reuse:
644: 
645: 1. **Extract Common Functionality**:
646:    - Create reusable helper functions for operations used across multiple tools
647:    - Build shared API clients for HTTP requests instead of duplicating code
648:    - Centralize error handling logic in utility functions
649:    - Extract business logic into dedicated functions that can be composed
650:    - Extract shared markdown or JSON field selection & formatting functionality
651: 
652: 2. **Avoid Duplication**:
653:    - NEVER copy-paste similar code between tools
654:    - If you find yourself writing similar logic twice, extract it into a function
655:    - Common operations like pagination, filtering, field selection, and formatting should be shared
656:    - Authentication/authorization logic should be centralized
657: 
658: ### Python-Specific Best Practices
659: 
660: 1. **Use Type Hints**: Always include type annotations for function parameters and return values
661: 2. **Pydantic Models**: Define clear Pydantic models for all input validation
662: 3. **Avoid Manual Validation**: Let Pydantic handle input validation with constraints
663: 4. **Proper Imports**: Group imports (standard library, third-party, local)
664: 5. **Error Handling**: Use specific exception types (httpx.HTTPStatusError, not generic Exception)
665: 6. **Async Context Managers**: Use `async with` for resources that need cleanup
666: 7. **Constants**: Define module-level constants in UPPER_CASE
667: 
668: ## Quality Checklist
669: 
670: Before finalizing your Python MCP server implementation, ensure:
671: 
672: ### Strategic Design
673: - [ ] Tools enable complete workflows, not just API endpoint wrappers
674: - [ ] Tool names reflect natural task subdivisions
675: - [ ] Response formats optimize for agent context efficiency
676: - [ ] Human-readable identifiers used where appropriate
677: - [ ] Error messages guide agents toward correct usage
678: 
679: ### Implementation Quality
680: - [ ] FOCUSED IMPLEMENTATION: Most important and valuable tools implemented
681: - [ ] All tools have descriptive names and documentation
682: - [ ] Return types are consistent across similar operations
683: - [ ] Error handling is implemented for all external calls
684: - [ ] Server name follows format: `{service}_mcp`
685: - [ ] All network operations use async/await
686: - [ ] Common functionality is extracted into reusable functions
687: - [ ] Error messages are clear, actionable, and educational
688: - [ ] Outputs are properly validated and formatted
689: 
690: ### Tool Configuration
691: - [ ] All tools implement 'name' and 'annotations' in the decorator
692: - [ ] Annotations correctly set (readOnlyHint, destructiveHint, idempotentHint, openWorldHint)
693: - [ ] All tools use Pydantic BaseModel for input validation with Field() definitions
694: - [ ] All Pydantic Fields have explicit types and descriptions with constraints
695: - [ ] All tools have comprehensive docstrings with explicit input/output types
696: - [ ] Docstrings include complete schema structure for dict/JSON returns
697: - [ ] Pydantic models handle input validation (no manual validation needed)
698: 
699: ### Advanced Features (where applicable)
700: - [ ] Context injection used for logging, progress, or elicitation
701: - [ ] Resources registered for appropriate data endpoints
702: - [ ] Lifespan management implemented for persistent connections
703: - [ ] Structured output types used (TypedDict, Pydantic models)
704: - [ ] Appropriate transport configured (stdio or streamable HTTP)
705: 
706: ### Code Quality
707: - [ ] File includes proper imports including Pydantic imports
708: - [ ] Pagination is properly implemented where applicable
709: - [ ] Filtering options are provided for potentially large result sets
710: - [ ] All async functions are properly defined with `async def`
711: - [ ] HTTP client usage follows async patterns with proper context managers
712: - [ ] Type hints are used throughout the code
713: - [ ] Constants are defined at module level in UPPER_CASE
714: 
715: ### Testing
716: - [ ] Server runs successfully: `python your_server.py --help`
717: - [ ] All imports resolve correctly
718: - [ ] Sample tool calls work as expected
719: - [ ] Error scenarios handled gracefully

(End of file - total 719 lines)
</content>
```

**Tool: bash**

**Input:**
```json
{
  "command": "cd /tmp/opencode 2>/dev/null && mkdir -p scctest/sub && printf 'package main\\nfunc main(){}\\n// comment\\n' > scctest/a.go && printf 'def f():\\n    return 1\\n' > scctest/sub/b.py && scc --format json2 scctest 2>&1 | head -c 1500; echo; echo \"=== json by-file ===\"; scc --format json --by-file scctest 2>&1 | head -c 800",
  "description": "Sample scc json2 and by-file output"
}
```

**Output:**
```
{"languageSummary":[{"Name":"Go","Bytes":38,"CodeBytes":0,"Lines":3,"Code":2,"Comment":1,"Blank":0,"Complexity":0,"Count":1,"WeightedComplexity":0,"Files":[],"LineLength":null,"ULOC":0},{"Name":"Python","Bytes":22,"CodeBytes":0,"Lines":2,"Code":2,"Comment":0,"Blank":0,"Complexity":0,"Count":1,"WeightedComplexity":0,"Files":[],"LineLength":null,"ULOC":0}],"estimatedCost":81.98951493094077,"estimatedScheduleMonths":0.38516092147778147,"estimatedPeople":0.01891176294931271}
=== json by-file ===
[{"Name":"Go","Bytes":38,"CodeBytes":0,"Lines":3,"Code":2,"Comment":1,"Blank":0,"Complexity":0,"Count":1,"WeightedComplexity":0,"Files":[{"Language":"Go","PossibleLanguages":["Go"],"Filename":"a.go","Extension":"go","Location":"scctest/a.go","Symlocation":"","Bytes":38,"Lines":3,"Code":2,"Comment":1,"Blank":0,"Complexity":0,"WeightedComplexity":0,"Hash":null,"Binary":false,"Minified":false,"Generated":false,"EndPoint":0,"Uloc":0}],"LineLength":null,"ULOC":0},{"Name":"Python","Bytes":22,"CodeBytes":0,"Lines":2,"Code":2,"Comment":0,"Blank":0,"Complexity":0,"Count":1,"WeightedComplexity":0,"Files":[{"Language":"Python","PossibleLanguages":["Python"],"Filename":"b.py","Extension":"py","Location":"scctest/sub/b.py","Symlocation":"","Bytes":22,"Lines":2,"Code":2,"Comment":0,"Blank":0,"Complexity
```

---

## Assistant (Plan · Claude Opus 4.8 · 3.9s)

I now have everything I need. Let me clean up my test directory (read-only constraint applies to the repo; this is my temp scratch in /tmp) and check the `--languages` output count for context.

**Tool: bash**

**Input:**
```json
{
  "command": "rm -rf /tmp/opencode/scctest; scc --languages 2>/dev/null | wc -l",
  "description": "Clean temp dir and count supported languages"
}
```

**Output:**
```
358

```

---

## Assistant (Plan · Claude Opus 4.8 · 192.2s)

I have enough to form a solid plan. A couple of design decisions genuinely need your input before I write the proposal — the repo can't answer these.

**Tool: question**

**Input:**
```json
{
  "questions": [
    {
      "header": "Tool granularity",
      "question": "scc is a single CLI with many flags. How should I shape the MCP tools?",
      "options": [
        {
          "label": "Few workflow tools (Recommended)",
          "description": "A small set of purpose-built tools (e.g. analyze_codebase, file_metrics, complexity_hotspots, cost_estimate, list_languages) that internally pick scc flags. Easier for an LLM to use well."
        },
        {
          "label": "One thin passthrough tool",
          "description": "A single run_scc tool exposing args/flags directly. Maximum flexibility, but the LLM must know scc's CLI."
        },
        {
          "label": "Both",
          "description": "Workflow tools plus one escape-hatch raw tool for advanced cases."
        }
      ]
    },
    {
      "header": "Path safety scope",
      "question": "scc reads the filesystem. Should the server restrict which paths can be scanned?",
      "options": [
        {
          "label": "Restrict to a configured root",
          "description": "Server takes a base/root dir (env or arg); reject paths outside it. Safer default for an MCP exposed to an LLM."
        },
        {
          "label": "Allow any path",
          "description": "No restriction; the LLM can scan any directory the process can read. Simpler, more flexible, less safe."
        }
      ]
    },
    {
      "header": "REQUIREMENTS.md state",
      "question": "REQUIREMENTS.md doesn't exist yet. The task says 'append' to it. How should I handle it?",
      "options": [
        {
          "label": "Create then append (Recommended)",
          "description": "Create REQUIREMENTS.md with a short intro and the proposed feature list."
        },
        {
          "label": "Create feature list only",
          "description": "Create the file containing just the proposed MCP feature list, no preamble."
        }
      ]
    }
  ]
}
```

**Output:**
```
User has answered your questions: "scc is a single CLI with many flags. How should I shape the MCP tools?"="Both", "scc reads the filesystem. Should the server restrict which paths can be scanned?"="We only want to scan directories that we have read and execute access to", "REQUIREMENTS.md doesn't exist yet. The task says 'append' to it. How should I handle it?"="It does exist. Please review the directory again with `ls .`". You can now continue with the user's answers in mind.
```

---

## Assistant (Plan · Claude Opus 4.8 · 4.8s)

The user says REQUIREMENTS.md exists. Let me re-check with a direct listing — it may be untracked/newly created since my first scan.

**Tool: bash**

**Input:**
```json
{
  "command": "ls -la /home/nicholas/Documents/projects/scc-mcp",
  "description": "Re-list repo directory contents"
}
```

**Output:**
```
total 48
drwxrwxr-x  3 nicholas nicholas 4096 Jun 24 14:18 .
drwxrwxr-x 19 nicholas nicholas 4096 Jun 24 14:11 ..
drwxrwxr-x  8 nicholas nicholas 4096 Jun 24 14:13 .git
-rw-rw-r--  1 nicholas nicholas 4628 Jun 24 14:11 .gitignore
-rw-rw-r--  1 nicholas nicholas    5 Jun 24 14:18 .python-version
-rw-rw-r--  1 nicholas nicholas  686 Jun 24 14:15 AGENTS.md
-rw-rw-r--  1 nicholas nicholas 1503 Jun 24 14:11 LICENSE
-rw-rw-r--  1 nicholas nicholas   80 Jun 24 14:11 README.md
-rw-rw-r--  1 nicholas nicholas  131 Jun 24 14:18 REQUIREMENTS.md
-rw-rw-r--  1 nicholas nicholas   85 Jun 24 14:18 main.py
-rw-rw-r--  1 nicholas nicholas  153 Jun 24 14:18 pyproject.toml

```

---

## Assistant (Plan · Claude Opus 4.8 · 4.3s)

New files appeared — looks like `uv init` was run. Let me read them all.

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/nicholas/Documents/projects/scc-mcp/REQUIREMENTS.md"
}
```

**Output:**
```
<path>/home/nicholas/Documents/projects/scc-mcp/REQUIREMENTS.md</path>
<type>file</type>
<content>
1: 1. Present a table of the top N files
2: 2. Count lines of code on the current working directory
3: 3. CLOC by extension | code feature
4: 

(End of file - total 4 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/nicholas/Documents/projects/scc-mcp/pyproject.toml"
}
```

**Output:**
```
<path>/home/nicholas/Documents/projects/scc-mcp/pyproject.toml</path>
<type>file</type>
<content>
1: [project]
2: name = "scc-mcp"
3: version = "0.1.0"
4: description = "Add your description here"
5: readme = "README.md"
6: requires-python = ">=3.14"
7: dependencies = []

(End of file - total 7 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/nicholas/Documents/projects/scc-mcp/main.py"
}
```

**Output:**
```
<path>/home/nicholas/Documents/projects/scc-mcp/main.py</path>
<type>file</type>
<content>
1: def main():
2:     print("Hello from scc-mcp!")
3: 
4: 
5: if __name__ == "__main__":
6:     main()

(End of file - total 6 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/nicholas/Documents/projects/scc-mcp/.python-version"
}
```

**Output:**
```
<path>/home/nicholas/Documents/projects/scc-mcp/.python-version</path>
<type>file</type>
<content>
1: 3.14

(End of file - total 1 lines)
</content>
```

---

## Assistant (Plan · Claude Opus 4.8 · 26.3s)

Now I have the full picture. The repo was `uv init`'d (Python 3.14, empty deps, placeholder `main.py`), and REQUIREMENTS.md already has 3 user-authored feature ideas I must preserve and append to.

Here's my plan.

---

# Plan: scc-mcp — dependencies + feature proposal

## Context (verified)
- `scc` v3.7.0 is installed at `/home/linuxbrew/.linuxbrew/bin/scc` — **assume present, do not install**.
- Repo was `uv init`'d: `pyproject.toml` (Python `>=3.14`, empty `dependencies`), placeholder `main.py`, `.python-version` = 3.14.
- `REQUIREMENTS.md` already contains 3 user ideas (top-N files, CWD line count, CLOC by extension) — **preserve and append below them**.
- `scc` exposes rich machine-readable output: `--format json2` (project summary + COCOMO cost), `--format json --by-file` (per-file stats incl. complexity), `--languages` (358 lines of supported langs).
- Decisions from you: build **both** workflow tools + a raw escape-hatch tool; **only scan dirs we have read+execute access to**; append to existing REQUIREMENTS.md.

## Step 1 — Add MCP dependencies via `uv`
Run (execution phase only):
```
uv add "mcp[cli]"
```
- Installs the official MCP Python SDK (FastMCP) + CLI extra. This creates/updates `uv.lock` and a `.venv`, and populates `pyproject.toml` `dependencies`.
- Verify import works: `uv run python -c "from mcp.server.fastmcp import FastMCP"`.
- No changes to `scc` itself; it stays an external PATH binary.

## Step 2 — Confirm scc CLI surface (already explored, recorded for design)
Key flags that map to features:
- `--format json2` → project summary + COCOMO `estimatedCost` / `estimatedScheduleMonths` / `estimatedPeople`.
- `--format json --by-file` → per-file `Code/Comment/Blank/Complexity` for top-N / hotspots.
- `-s/--sort {files,name,lines,blanks,code,comments,complexity}` and `-p/--percent`.
- `-i/--include-ext`, `-x/--exclude-ext`, `--exclude-dir`, `-M/--not-match` → filtering.
- `-l/--languages`, `-w/--wide`, `-u/--uloc`, `-a/--dryness`, `--cocomo-project-type`, `--no-cocomo`.

## Step 3 — Append proposed MCP features to `REQUIREMENTS.md`
Preserve the existing 3 lines, then append a new section. Proposed features (the actual deliverable for this task):

**Workflow tools**
1. `scc_count_lines` — summary CLOC for a path (defaults to CWD). Covers existing req #2.
2. `scc_top_files` — top-N files by a sortable metric (code/complexity/lines), table or JSON. Covers req #1.
3. `scc_by_extension` — breakdown by language/extension. Covers req #3.
4. `scc_complexity_hotspots` — files ranked by complexity (per-file json), to find refactor targets.
5. `scc_cost_estimate` — COCOMO cost/schedule/people from `json2`, with configurable project type.
6. `scc_list_languages` — supported languages/extensions (`--languages`), useful for filtering decisions.
7. `scc_file_metrics` — detailed stats for a single file or subset (by-file, filtered).

**Escape-hatch tool**
8. `scc_run` — thin passthrough accepting a validated arg list + target path; returns raw stdout in the chosen `--format`. Flexibility for advanced/unsupported flag combos.

**Cross-cutting requirements (apply to all tools)**
- **Path safety**: resolve the target path; reject if it doesn't exist or the process lacks **read + execute (`os.access`, R_OK|X_OK)** on it; only scan accessible dirs. Default target = CWD.
- **scc presence check**: detect `scc` on PATH at startup / per call; fail with a clear, actionable error if missing (per AGENTS.md key constraint).
- **Structured output**: prefer `--format json2` / `json` internally, parse, and offer markdown-table vs JSON response formats to the caller.
- **Safe invocation**: call scc via `subprocess` with an argument list (no shell), enforce a timeout, surface non-zero exit + stderr clearly.
- **Filtering passthrough**: include/exclude extensions, exclude dirs, sort, percent, top-N limits as validated Pydantic fields.

## Step 4 — (Optional, recommend) note follow-ups in `AGENTS.md`
Once deps are added, update AGENTS.md "Current state" with the real run command (`uv run ...`) and that `mcp[cli]` is the dependency. *(I'll only do this if you want it in this pass.)*

## What I will NOT do
- Will not install or modify `scc`.
- Will not implement the server code yet — this task is deps + CLI exploration + feature proposal only. (Tool implementation can be a follow-up.)

---

Two things to confirm before I execute:
1. Scope of this pass — just **(a) `uv add mcp[cli]`** and **(b) append features to REQUIREMENTS.md**, leaving server implementation for later? Or do you also want a starter `server.py` scaffold now?
2. Should I also refresh `AGENTS.md` (Step 4) in this pass?

---

## User

1. use `uv add fastmcp`. Why did you choose `mcp[cli]` instaed of `fastmcp`. Do not add server scaffolding. 2. Yes

---

## Assistant (Plan · Claude Opus 4.8 · 30.2s)

Good questions on the dependency choice. Let me clarify why I originally suggested `mcp[cli]`, then explain the difference now that you've chosen `fastmcp`.

**Why I originally suggested `mcp[cli]`:** It's the official Anthropic/MCP Python SDK (`modelcontextprotocol/python-sdk`). FastMCP was originally a separate project by Prefect/jlowin that got merged *into* the official SDK as `mcp.server.fastmcp` (the "FastMCP 1.0" API). The mcp-builder skill docs reference `from mcp.server.fastmcp import FastMCP`, so I defaulted to that.

**`fastmcp` (the standalone package) vs `mcp[cli]`:**
- `fastmcp` is the **independent, actively-developed v2** package (`jlowin/fastmcp`). It's a superset of the SDK's FastMCP — more features (auth, server composition, richer client, deployment helpers), faster-moving, `import` is `from fastmcp import FastMCP`.
- `mcp[cli]` is the **official SDK** with the frozen FastMCP 1.0 API baked in, plus the `mcp` CLI dev tools.

Both are valid. `fastmcp` (standalone) is a reasonable, arguably better choice for a greenfield server — just note the import path and docs differ from the skill's examples. Your call is honored.

Here's the updated plan.

---

# Plan: scc-mcp — add deps + propose features (revised)

## Scope confirmed
- **(a)** `uv add fastmcp` — standalone FastMCP v2, **not** `mcp[cli]`.
- **(b)** Append proposed MCP features to `REQUIREMENTS.md` (preserve existing 3 lines).
- **(c)** Refresh `AGENTS.md` with verified setup/run facts.
- **No server scaffolding.** No `scc` install/changes.

## Step 1 — Add dependency
```
uv add fastmcp
```
- Populates `pyproject.toml` `dependencies`, creates `uv.lock` + `.venv`.
- Verify: `uv run python -c "from fastmcp import FastMCP; print('ok')"`.
- Note: requires-python is `>=3.14`; if `fastmcp`'s resolver complains about 3.14, I'll report back rather than silently change the pin.

## Step 2 — Append features to `REQUIREMENTS.md`
Keep the existing 3 numbered lines, then add a `## Proposed MCP features` section:

**Workflow tools**
1. `scc_count_lines` — summary CLOC for a path (default CWD). [covers existing #2]
2. `scc_top_files` — top-N files by sortable metric (code/complexity/lines). [covers #1]
3. `scc_by_extension` — language/extension breakdown. [covers #3]
4. `scc_complexity_hotspots` — files ranked by complexity (refactor targets).
5. `scc_cost_estimate` — COCOMO cost/schedule/people (`json2`), configurable project type.
6. `scc_list_languages` — supported languages/extensions (`--languages`).
7. `scc_file_metrics` — detailed per-file stats for a file/subset.

**Escape-hatch tool**
8. `scc_run` — validated passthrough (arg list + target path), returns raw scc output in chosen `--format`.

**Cross-cutting requirements**
- Path safety: only scan paths the process has **read + execute** access to (`os.access(..., R_OK|X_OK)`); reject otherwise; default to CWD.
- `scc` presence check with a clear error if missing from PATH.
- Invoke via `subprocess` argument list (no shell), with timeout; surface non-zero exit + stderr.
- Prefer JSON formats internally; offer markdown-table vs JSON output to callers.
- Filtering passthrough: include/exclude ext, exclude dirs, sort, percent, top-N.

## Step 3 — Refresh `AGENTS.md`
- Update **Current state**: now a `uv` project (Python 3.14), dep = `fastmcp`.
- Add **Commands**: `uv sync`, `uv run python -c "from fastmcp import FastMCP"`, run via `uv run`.
- Keep the **Key constraint** (external `scc` binary on PATH).
- Note: standalone `fastmcp` import is `from fastmcp import FastMCP` (differs from the SDK's `mcp.server.fastmcp`).

## What I will NOT do
- No server implementation/scaffolding.
- No `scc` install or modification.
- No changing the Python version pin unless resolution forces it (will ask first).

---

Ready to execute on your approval. Anything to adjust before I switch out of plan mode?

---

## User

Implement this plan

---

## Assistant (Build · Claude Opus 4.8 · 3.3s)

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Run `uv add fastmcp` and verify import",
      "status": "in_progress",
      "priority": "high"
    },
    {
      "content": "Append proposed MCP features to REQUIREMENTS.md",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Refresh AGENTS.md with verified setup/run facts",
      "status": "pending",
      "priority": "medium"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Run `uv add fastmcp` and verify import",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Append proposed MCP features to REQUIREMENTS.md",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Refresh AGENTS.md with verified setup/run facts",
    "status": "pending",
    "priority": "medium"
  }
]
```

---

## Assistant (Build · Claude Opus 4.8 · 4.2s)

**Tool: bash**

**Input:**
```json
{
  "command": "uv add fastmcp",
  "description": "Add fastmcp dependency via uv",
  "timeout": 180000
}
```

**Output:**
```
Using CPython 3.14.5 interpreter at: /home/linuxbrew/.linuxbrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
Resolved 72 packages in 216ms
Downloading beartype (1.3MiB)
 Downloaded beartype
Prepared 29 packages in 303ms
Installed 68 packages in 14ms
 + aiofile==3.11.1
 + annotated-types==0.7.0
 + anyio==4.14.0
 + attrs==26.1.0
 + authlib==1.7.2
 + beartype==0.22.9
 + cachetools==7.1.4
 + caio==0.9.25
 + certifi==2026.6.17
 + cffi==2.0.0
 + click==8.4.2
 + cryptography==49.0.0
 + cyclopts==4.19.0
 + dnspython==2.8.0
 + docstring-parser==0.18.0
 + email-validator==2.3.0
 + exceptiongroup==1.3.1
 + fastmcp==3.4.2
 + fastmcp-slim==3.4.2
 + griffelib==2.1.0
 + h11==0.16.0
 + httpcore==1.0.9
 + httpx==0.28.1
 + httpx-sse==0.4.3
 + idna==3.18
 + jaraco-classes==3.4.0
 + jaraco-context==6.1.2
 + jaraco-functools==4.5.0
 + jeepney==0.9.0
 + joserfc==1.7.1
 + jsonref==1.1.0
 + jsonschema==4.26.0
 + jsonschema-path==0.5.0
 + jsonschema-specifications==2025.9.1
 + keyring==25.7.0
 + markdown-it-py==4.2.0
 + mcp==1.28.0
 + mdurl==0.1.2
 + more-itertools==11.1.0
 + openapi-pydantic==0.5.1
 + opentelemetry-api==1.43.0
 + packaging==26.2
 + pathable==0.6.0
 + platformdirs==4.10.0
 + py-key-value-aio==0.4.5
 + pycparser==3.0
 + pydantic==2.13.4
 + pydantic-core==2.46.4
 + pydantic-settings==2.14.2
 + pygments==2.20.0
 + pyjwt==2.13.0
 + pyperclip==1.11.0
 + python-dotenv==1.2.2
 + python-multipart==0.0.32
 + pyyaml==6.0.3
 + referencing==0.37.0
 + rich==15.0.0
 + rich-rst==2.0.1
 + rpds-py==2026.5.1
 + secretstorage==3.5.0
 + sse-starlette==3.4.5
 + starlette==1.3.1
 + typing-extensions==4.15.0
 + typing-inspection==0.4.2
 + uncalled-for==0.3.2
 + uvicorn==0.49.0
 + watchfiles==1.2.0
 + websockets==16.0

```

---

## Assistant (Build · Claude Opus 4.8 · 5.3s)

fastmcp 3.4.2 installed. Verifying the import:

**Tool: bash**

**Input:**
```json
{
  "command": "uv run python -c \"from fastmcp import FastMCP; print('ok', __import__('fastmcp').__version__)\"",
  "description": "Verify fastmcp import works"
}
```

**Output:**
```
ok 3.4.2

```

---

## Assistant (Build · Claude Opus 4.8 · 2.6s)

Import works. Let me verify pyproject.toml was updated, then proceed.

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/nicholas/Documents/projects/scc-mcp/pyproject.toml"
}
```

**Output:**
```
<path>/home/nicholas/Documents/projects/scc-mcp/pyproject.toml</path>
<type>file</type>
<content>
1: [project]
2: name = "scc-mcp"
3: version = "0.1.0"
4: description = "Add your description here"
5: readme = "README.md"
6: requires-python = ">=3.14"
7: dependencies = [
8:     "fastmcp>=3.4.2",
9: ]

(End of file - total 9 lines)
</content>
```

---

## Assistant (Build · Claude Opus 4.8 · 6.0s)

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Run `uv add fastmcp` and verify import",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Append proposed MCP features to REQUIREMENTS.md",
      "status": "in_progress",
      "priority": "high"
    },
    {
      "content": "Refresh AGENTS.md with verified setup/run facts",
      "status": "pending",
      "priority": "medium"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Run `uv add fastmcp` and verify import",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Append proposed MCP features to REQUIREMENTS.md",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Refresh AGENTS.md with verified setup/run facts",
    "status": "pending",
    "priority": "medium"
  }
]
```

---

## Assistant (Build · Claude Opus 4.8 · 13.3s)

**Tool: edit**

**Input:**
```json
{
  "filePath": "/home/nicholas/Documents/projects/scc-mcp/REQUIREMENTS.md",
  "oldString": "1. Present a table of the top N files\n2. Count lines of code on the current working directory\n3. CLOC by extension | code feature\n",
  "newString": "1. Present a table of the top N files\n2. Count lines of code on the current working directory\n3. CLOC by extension | code feature\n\n## Proposed MCP features\n\nTools wrap the external `scc` binary (assumed installed and on `PATH`).\nWorkflow tools cover common tasks; one passthrough tool is an escape hatch.\n\n### Workflow tools\n\n1. `scc_count_lines` — summary CLOC (code/comment/blank/total) for a path,\n   defaulting to the current working directory. [covers requirement #2]\n2. `scc_top_files` — table of the top N files sorted by a chosen metric\n   (`code`, `complexity`, `lines`, ...). Backed by `--by-file`. [covers requirement #1]\n3. `scc_by_extension` — breakdown of CLOC per language/extension. [covers requirement #3]\n4. `scc_complexity_hotspots` — files ranked by cyclomatic complexity to surface\n   refactor targets (per-file JSON, sorted by `complexity`).\n5. `scc_cost_estimate` — COCOMO cost / schedule / people estimates from\n   `--format json2`, with configurable project type (organic, semi-detached, embedded).\n6. `scc_list_languages` — supported languages and their extensions (`--languages`),\n   useful for choosing include/exclude filters.\n7. `scc_file_metrics` — detailed per-file stats for a single file or filtered subset.\n\n### Escape-hatch tool\n\n8. `scc_run` — validated passthrough accepting an argument list plus a target path;\n   returns raw `scc` output in the requested `--format`. For advanced or unsupported\n   flag combinations.\n\n### Cross-cutting requirements (apply to all tools)\n\n- **Path safety**: resolve the target path and only scan paths the process has both\n  read and execute access to (`os.access(path, os.R_OK | os.X_OK)`); reject otherwise.\n  Default target is the current working directory.\n- **`scc` presence check**: verify `scc` is on `PATH`; fail with a clear, actionable\n  error if it is missing (it is an external binary, not a Python dependency).\n- **Safe invocation**: call `scc` via `subprocess` with an argument list (never the\n  shell), enforce a timeout, and surface non-zero exit codes plus `stderr` clearly.\n- **Structured output**: prefer JSON formats (`json`, `json2`) internally; offer the\n  caller a choice between a human-readable markdown table and machine-readable JSON.\n- **Filtering passthrough**: expose include/exclude extensions, exclude directories,\n  sort column, percentage values, and top-N limits as validated parameters.\n"
}
```

**Output:**
```
Edit applied successfully.
```

---

## Assistant (Build · Claude Opus 4.8 · 3.5s)

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Run `uv add fastmcp` and verify import",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Append proposed MCP features to REQUIREMENTS.md",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Refresh AGENTS.md with verified setup/run facts",
      "status": "in_progress",
      "priority": "medium"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Run `uv add fastmcp` and verify import",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Append proposed MCP features to REQUIREMENTS.md",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Refresh AGENTS.md with verified setup/run facts",
    "status": "in_progress",
    "priority": "medium"
  }
]
```

---

## Assistant (Build · Claude Opus 4.8 · 8.4s)

**Tool: write**

**Input:**
```json
{
  "filePath": "/home/nicholas/Documents/projects/scc-mcp/AGENTS.md",
  "content": "# AGENTS.md\n\n## What this is\nMCP (Model Context Protocol) server that exposes [`boyter/scc`](https://github.com/boyter/scc)\n(a code-counting / complexity tool) to an LLM. Python project managed with `uv`.\n\n## Current state\n`uv` project (Python 3.14). Dependency: `fastmcp` (standalone FastMCP v2).\nServer not implemented yet — `main.py` is the `uv init` placeholder. Planned tools\nare listed in `REQUIREMENTS.md`.\n\n## Commands\n- Install deps: `uv sync`\n- Add a dep: `uv add <pkg>` (do not edit `pyproject.toml` deps by hand)\n- Run anything in the venv: `uv run <cmd>` (e.g. `uv run python main.py`)\n- Verify framework import: `uv run python -c \"from fastmcp import FastMCP\"`\n\n## Conventions / gotchas\n- Import is `from fastmcp import FastMCP` (standalone v2), NOT the official SDK's\n  `from mcp.server.fastmcp import FastMCP`. The two APIs differ; follow fastmcp v2 docs.\n- `scc` is an external binary, not a Python dependency. Assume it is installed and on\n  `PATH` — do NOT install it. Invocations must fail clearly if it is missing.\n- Only scan paths with read + execute access (`os.access(p, os.R_OK | os.X_OK)`); default\n  to the current working directory.\n- Useful `scc` machine-readable output: `--format json2` (project summary + COCOMO),\n  `--format json --by-file` (per-file stats incl. complexity), `--languages`.\n"
}
```

**Output:**
```
Wrote file successfully.
```

---

## Assistant (Build · Claude Opus 4.8 · 3.0s)

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Run `uv add fastmcp` and verify import",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Append proposed MCP features to REQUIREMENTS.md",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Refresh AGENTS.md with verified setup/run facts",
      "status": "completed",
      "priority": "medium"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Run `uv add fastmcp` and verify import",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Append proposed MCP features to REQUIREMENTS.md",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Refresh AGENTS.md with verified setup/run facts",
    "status": "completed",
    "priority": "medium"
  }
]
```

---

## Assistant (Build · Claude Opus 4.8 · 7.2s)

Done. All three steps complete.

**1. Dependency added** — `uv add fastmcp` installed `fastmcp==3.4.2` (standalone FastMCP v2, with Python 3.14). `pyproject.toml` now lists `fastmcp>=3.4.2`, and the import verifies:
```
$ uv run python -c "from fastmcp import FastMCP; print('ok')"
ok 3.4.2
```
Note: `uv` also created `.venv` and `uv.lock`. No scaffolding added; `scc` untouched.

**2. `REQUIREMENTS.md`** — preserved your original 3 lines and appended a `## Proposed MCP features` section: 7 workflow tools (`scc_count_lines`, `scc_top_files`, `scc_by_extension`, `scc_complexity_hotspots`, `scc_cost_estimate`, `scc_list_languages`, `scc_file_metrics`), the `scc_run` escape-hatch, and cross-cutting requirements (path safety with R_OK|X_OK, scc presence check, safe subprocess invocation, structured output, filtering).

**3. `AGENTS.md`** — updated to reflect the `uv`/`fastmcp` setup, real commands, and the key gotchas (correct import path for standalone fastmcp vs the SDK, external `scc` binary, path-access rule, useful scc JSON formats).

The first three requirements map to tools 1-3 as noted inline. Server implementation remains a follow-up when you're ready.

---

