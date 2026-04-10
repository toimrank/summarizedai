import asyncio
from fastmcp import Client

async def main():
    client = Client("http://localhost:5000/mcp")
    async with client:

        resources = await client.list_resources()
        for resource in resources:
            content = await client.read_resource(resource.uri)
            print(content[0].text)

        tools = await client.list_tools()
        for tool in tools:
            print(tool.name)
            print(tool.description)

        result_add = await client.call_tool("add_numbers", {"a" : 5, "b" : 6})
        print("5 +6 = ", result_add.structured_content["result"])

        result_message = await client.call_tool("greet", {"name": "Mike"})
        print("Name = ", result_message.structured_content["result"])

        prompts = await client.list_prompts()
        print(prompts)

        result = await client.get_prompt(
            "welcome_message",
            arguments={"topic" : "Python"}
        )
        print(result.description)

asyncio.run(main())