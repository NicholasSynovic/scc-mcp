"""scc MCP server.

Exposes the external ``scc`` code-counting tool as MCP tools. Tool definitions
live here; the scc invocation/safety layer is in ``runner``, shared input models
in ``models``, and output rendering in ``format``.
"""

from fastmcp import FastMCP

from .tools import byfile, summary

mcp = FastMCP("scc_mcp")

summary.register(mcp)
byfile.register(mcp)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
