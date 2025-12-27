from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI

# Shared state
class AgentState(TypedDict):
    question: str
    need_search: bool
    context: Optional[str]
    answer: Optional[str]

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key="<API_KEY>"
)

def decide_search(state: AgentState) -> AgentState:
    """Decide whether the question needs external data"""
    prompt = f"""
    Decide if this question needs external or up-to-date information.
    Answer only Yes or No.

    Question: {state['question']}
    """
    response = llm.invoke(prompt).content.lower()

    state["need_search"] = "yes" in response
    return state

def search_node(state: AgentState) -> AgentState:

    print(" SEARCH NODE >>>>>>>>>>>>>>>>>..")

    """Simulated RAG / search step"""
    state["context"] = (
        "LangGraph is a framework built on LangChain that allows you "
        "to build stateful, multi-step AI workflows using graphs."
    )
    return state


def generate_answer(state: AgentState) -> AgentState:

    """Generate final answer using LLM"""
    prompt = f"""
    Use the following context if available to answer the question.

    Context:
    {state.get('context', '')}

    Question:
    {state['question']}
    """
    state["answer"] = llm.invoke(prompt).content
    return state

graph = StateGraph(AgentState)

graph.add_node("decide_search", decide_search)
graph.add_node("search", search_node)
graph.add_node("generate_answer", generate_answer)

graph.set_entry_point("decide_search")

def route(state: AgentState):
    if state["need_search"]:
        return "search"
    return "generate_answer"

graph.add_conditional_edges(
    "decide_search",
    route,
    {
        "search": "search",
        "generate_answer": "generate_answer",
    }
)

graph.add_edge("search", "generate_answer")
graph.add_edge("generate_answer", END)

app = graph.compile()

result = app.invoke({
    "question": "What is langchain ?"
})

print("Final Answer:\n", result["answer"])
