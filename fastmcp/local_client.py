from fastmcp.client.transports import StreamableHttpTransport
from fastmcp import Client
import asyncio

async def main():
    async with Client("http://localhost:5000/mcp") as client:
        print(">>>>>>>>>>>>>>>>>>")
        # Call a tool
        tools = await client.list_tools()   
        resources = await client.list_resources()   
        print(tools)

asyncio.run(main())