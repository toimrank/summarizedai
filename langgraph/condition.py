from typing import TypedDict
from langgraph.graph import StateGraph, END

class State(TypedDict):
    question: str
    answer: str
    need_search: str

def search_tool(query: str) -> str:
    return f"Search result for '{query}'"

def external_search_node(state:  State):
    result = search_tool(state["question"])    
    return {
        "question" : state["question"],
        "answer" : f"{result} - from external search"
    }

def generate_answer(state: State):
    return {
        "question" : state["question"],
        "answer" : "The response is from generate answer"
    }

def check_node(state: State):

    need_search = "no"

    if "need search"  in state["question"].lower():
        need_search = "yes"

    return {
        "question" : state["question"],
        "answer" : "",
        "need_search" : need_search
    }        

def route(state: State):
    if "yes" in state["need_search"]:
        return "external_search_node"
    return "generate_answer"

graph = StateGraph(State)

graph.add_node("check_node", check_node)
graph.add_node("external_search_node", external_search_node)
graph.add_node("generate_answer", generate_answer)

graph.set_entry_point("check_node")

graph.add_conditional_edges(
    "check_node",
    route,{
        "external_search_node" : "external_search_node",
        "generate_answer" : "generate_answer"
    }
)

app = graph.compile()

result = app.invoke({
    "question" : "What is Langgraph need search ?"
})

print(result["answer"])