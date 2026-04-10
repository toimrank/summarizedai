from fastmcp.client.transports import StreamableHttpTransport
from fastmcp import Client
import asyncio

url = "https://satisfactory-red-alligator.fastmcp.app/mcp"
headers = {"Authorization": "Bearer TOKEN_VALUE"}


transport = StreamableHttpTransport(url=url, headers=headers)

async def main():
    async with Client(transport=transport) as client:
        print(">>>>>>>>>>>>>>>>>>")
        # Call a tool
        tools = await client.list_tools()    
        print(tools)

asyncio.run(main())