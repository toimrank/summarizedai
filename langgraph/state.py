from typing import TypedDict
from langgraph.graph import StateGraph, END

class GreetingState(TypedDict):
    name: str
    message: str

def read_name(state: GreetingState) -> GreetingState:
    print("read_name >>>>>>>>>>>>>")
    state["name"] = state["name"].title()
    return state

def generate_greeting(state: GreetingState) -> GreetingState:
    print("generate_greeting >>>>>>>>>>>>>")
    state["message"]= f"Hello {state['name']}! Welcome to LangGraph!"
    return state

graph = StateGraph(GreetingState)

graph.add_node("read_name", read_name)
graph.add_node("generate_greeting", generate_greeting)

graph.set_entry_point("read_name")

graph.add_edge("read_name", "generate_greeting")
graph.add_edge("generate_greeting", END)

app = graph.compile()

result = app.invoke({
    "name" :  "Mike",
    "message" : ""
})

print(result["message"])