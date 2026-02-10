# Add the following instruction into your client when require to use this MCP server.
# Add into your json configuration.

  "mcpServers": {
	  "gitaddition": {
		  "command": "uvx",
		  "args": [
		  "--from",
		  "git+https://github.com/macgpta/mcp-deployment.git",
		  "mcp-server"
		  ]
	  }
  }