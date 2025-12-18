from typing import Any
from langgraph.store.memory import InMemoryStore
from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from langchain_openai import ChatOpenAI

@tool
def get_user_info(user_id: str, runtime: ToolRuntime)-> str:
    """Look up user info from memort"""
    store = runtime.store
    user_info = store.get(("users",), user_id)
    return str(user_info.value) if user_info else "Unknown User"

@tool
def save_user_info(user_id: str, user_info: dict[str, Any], runtime: ToolRuntime) -> str:
    """Save userinfo into memory"""
    store = runtime.store
    store.put(("users",), user_id, user_info)
    return "Successfully Save user Info."

store = InMemoryStore()

model = ChatOpenAI(
    model="gpt-4o",
    api_key="<API_KEY>"
)

agent = create_agent(
    model,
    tools=[get_user_info, save_user_info],
    store=store
)

agent.invoke({
    "messages" : [
        {
            "role" : "user",
            "content" : (
                "Save the following user:"
                "userid: user123, name: Rob, age: 20, email: rob@test.com"
            )
        }
    ]
})

response = agent.invoke({
    "messages" : [
        {
            "role" : "user",
            "content" : "Get user info for user with id 'user123'"
        }
    ]
})

messages = response["messages"]
print(messages[3].content)