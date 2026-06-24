"""Minimal scc MCP server."""

from fastmcp import FastMCP

mcp = FastMCP("scc_mcp")


@mcp.tool
def hello_world() -> str:
    """Return a simple greeting to confirm the server is reachable."""
    return "Hello world"


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
