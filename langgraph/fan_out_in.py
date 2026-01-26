from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class BlogState(TypedDict):
    topic: str
    intro: str
    examples: str
    code: str
    final_blog: str

def planner(state: BlogState):
    return state

def write_intro(state: BlogState):
    return {
        "intro" :  f"Intro about {state['topic']}"
    }

def write_examples(state):
    return {
        "examples" :  "Real-world Examples"
    }

def write_code(state: BlogState):
    return {
        "code" : "LangGaph Code Snippet"
    }

def merge_content(state: BlogState):
    final = (
        state['intro'] + "\n" +
        state['examples'] + "\n" +
        state['code'] + "\n"
    )

    return {
        "final_blog" : final
    }

graph = StateGraph(BlogState)

graph.add_node("planner", planner)
graph.add_node("write_intro", write_intro)
graph.add_node("write_examples", write_examples)
graph.add_node("write_code", write_code)
graph.add_node("merge", merge_content)

graph.add_edge(START, "planner")

graph.add_edge("planner", "write_intro")
graph.add_edge("planner", "write_examples")
graph.add_edge("planner", "write_code")

graph.add_edge("write_intro", "merge")
graph.add_edge("write_examples", "merge")
graph.add_edge("write_code", "merge")

graph.add_edge("merge", END)

app = graph.compile()

result = app.invoke({
    "topic" : "Explain LangGraph Workflows"
})

print(result['final_blog'])