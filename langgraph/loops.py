from typing import TypedDict
from langgraph.graph import StateGraph, END

class GrpahState(TypedDict):
    question: str
    answer: str
    score: int
    retries: int

def generate_answer(state: GrpahState):
    if not state["answer"]:
        state["answer"] = f"Initialize answer for: {state['question']}"
    else:
        state["answer"] += " (improved)"

    return state

def evaluate_answer(state: GrpahState):

    state["score"] += 1
    state["retries"] += 1

    return state

def should_continue(state: GrpahState):

    """"Controls the loop"""

    if state["score"] >=3 or state["retries"] >=5:
        return "end"
    return "continue"

graph = StateGraph(GrpahState)

graph.add_node("generate_answer", generate_answer)
graph.add_node("evaluate_answer", evaluate_answer)

graph.set_entry_point("generate_answer")

graph.add_edge("generate_answer", "evaluate_answer")

graph.add_conditional_edges(
    "evaluate_answer",
    should_continue,
    {
        "continue" : "generate_answer",
        "end" : END
    }
)

app = graph.compile()

result = app.invoke({
    "question": "Explain loops in langgraph",
    "answer" : "",
    "score" : 0,
    "retries" : 0,
})

print(">>>>>>> Final Response")
print("Answer: ",result["answer"])
print("Score: ",result["score"])
print("Retries: ",result["retries"])