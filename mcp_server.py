from fastmcp import FastMCP
from fastmcp.server.context import Context
from fastmcp.dependencies import CurrentContext

mcp = FastMCP("my-fastmcp")

@mcp.tool()
def add_numbers(a: int, b: int, ctx: Context) -> int:
    """
        Add two numbers and return the result
    """
    ctx.set_state("counter", 123)
    print(ctx.get_state("counter"))
    return a + b

@mcp.tool() 
def greet(name: str) -> str:
    """
    Greet a user
    """
    return f"Hello, {name}! Welcome to FastMCP"

@mcp.resource("resource://greeting")
def get_greeting(ctx: Context = CurrentContext()) -> str:
    """Provides a simple greeting message."""
    print(ctx.fastmcp.name)
    print(ctx.request_id)
    print(ctx.client_id)
    print(ctx.request_context)
    print(ctx.session_id)

    print(ctx.list_prompts())
    print(ctx.list_resources())

    ctx.debug("")
    ctx.info()
    ctx.error("")
    return "Hello from FastMCP Resources!"

@mcp.resource("resource://app/config")
def app_config() -> dict:
    return {
        "app_name": "FastMCP Demo",
        "version": "1.0.0",
        "features": ["resources", "tools", "prompts"],
        "env": "production"
    }

@mcp.prompt()
def welcome_message(topic: str):
    """Hello! I am you assistant.
    How can I help you today ?"""
    print(topic)

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port="5000", path="/mcp")
