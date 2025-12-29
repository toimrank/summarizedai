from langgraph.graph import StateGraph, END
from typing import TypedDict

class GraphState(TypedDict):
    user_query: str
    location: str
    restaurant_data: str
    final_response: str

def restaurat_search_tool(query: str, location: str) -> str:
    """
      Simulates an external API like Google maps / Yelp
    """
    return(
        f"Top Restaurants in {location}"
        f"1. Italian Bistro 4.5\n"
        f"2. Vegas Cafe 4.4"
    )

def tool_node(state: GraphState):
    result = restaurat_search_tool(
        state["user_query"],
        state["location"]
    )

    state["restaurant_data"] = result
    return state

def response_node(state: GraphState):

    state["final_response"] = (
        f"Your Quesry: {state['user_query']}\n\n"
        f"{state['restaurant_data']}\n\n"
        f"Enjoy your meal!"
    )

    return state

graph = StateGraph(GraphState)

graph.add_node("tool_node", tool_node)
graph.add_node("response_node", response_node)

graph.set_entry_point("tool_node")

graph.add_edge("tool_node", "response_node")
graph.add_edge("response_node", END)

app =  graph.compile()

result = app.invoke({
    "user_query" : "Suggest good restaurant near me",
    "location" : "Phoenix",
    "restaurant_data" : "",
    "final_response" : ""
})

print(result["final_response"])