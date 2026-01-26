from typing import TypedDict, List

from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Evaluates a math expression"""
    return str(eval(expression))

tools = [calculator]
toolMap = {tool.name : tool for tool in tools}

class AgentState(TypedDict):
    messages : List

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="<API_KEY>"
)

llm_with_tools = llm.bind_tools(tools)

def reason(state: AgentState):
    """LLM thinks and decides next action"""
    response = llm_with_tools.invoke(state["messages"])

    print(response)

    return {
        "messages" : state["messages"] + [response]
    }

def act(state: AgentState):
    """Execute tool calls"""

    last_message = state["messages"][-1]

    if not last_message.tool_calls:
        return state

    tool_call = last_message.tool_calls[0]
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    result = toolMap[tool_name].invoke(tool_args)

    tool_message = ToolMessage(
        content=result,
        tool_call_id = tool_call["id"]
    )

    return {
        "messages" : state["messages"] + [tool_message]
    }

def should_continue(state: AgentState):
    """Decide whetehr to continue or finish"""
    last_message = state["messages"][-1]

    if isinstance(last_message, AIMessage) and not last_message.tool_calls:
        return "end"
    return "continue"

graph = StateGraph(AgentState)

graph.add_node("reason", reason)
graph.add_node("act", act)

graph.add_edge(START, "reason")
graph.add_edge("reason", "act")

graph.add_conditional_edges(
    "act",
    should_continue,
    {
        "continue": "reason",
        "end" : END
    }
)

app = graph.compile()

user_input = "What is (25 * 4) + 10 ?"

result = app.invoke({
    "messages" : [HumanMessage(content=user_input)]
})

print("\nFinal Answer: \n")
print(result["messages"][-1].content)


