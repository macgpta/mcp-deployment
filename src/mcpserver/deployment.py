# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP Server instance
mcp = FastMCP("Demo")

# Add an additional tool to the server
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b