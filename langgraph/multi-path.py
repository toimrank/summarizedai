from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_postgres import PGVector
from langgraph.graph import StateGraph, END
from typing import TypedDict, List
import os

os.environ["OPENAI_API_KEY"] = "<API_KEY>"

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/postgres"

COLLECTION_NAME = "langgraph_docs"

llm = ChatOpenAI(temperature=0.4)

class RAGState(TypedDict):
    question: str
    search_type: str
    documents: List[str]
    tool_result: str
    answer: str

RAW_DOCUMENTS = [
    "LangGraph is a framework for building stateful AI workflows.",
    "RAG retrieves relevant documents from a vector database to ground LLM output."
]

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

texts = []
for doc in RAW_DOCUMENTS:
    texts.extend(splitter.split_text(doc))

print(texts)

pgvector_store = PGVector(
    connection=DATABASE_URL,
    embeddings=embedding_model,
    collection_name=COLLECTION_NAME
)

#pgvector_store.add_texts(texts)
print("Documents Successfully Stored in PGVector")

retriever = pgvector_store.as_retriever(
    search_kwargs={"k":1}
)

def pgvector_tool(query: str) -> List[str]:
    docs = retriever._get_relevant_documents(query, run_manager=None)
    return[doc.page_content for doc in docs]

def pgvector_node(state:  RAGState):
    state["documents"] = pgvector_tool(state["question"])
    return state

def pgvector_answer_node(state: RAGState):
    context = "\n".join(state["documents"])
    prompt = (
        "return the reponse from tool as is :\n\n"
        f"{context}"
    )
    state["answer"] = llm.invoke(prompt).content.lower()
    return state

def calculator_tool(expression: str) -> str:
    return str(eval(expression))

def calculator_node(state: RAGState):
    state["tool_result"] = calculator_tool(state["question"])
    return state

def calculator_answer_node(state: RAGState):
    state["answer"] = f"calculation result: {state['tool_result']}"
    return state

def clarify_node(state: RAGState):
    state["answer"] = "Please prvoide more ddetails so I can help accurately."
    return state

def decide_search(state: RAGState) -> RAGState:
    q = state["question"].lower()

    search_type = "direct"

    if any(op in q for  op in ["+", "-", "*", "/"]):
        search_type = "math"
    elif any(word in q for word in ["langgraph", "rag", "vector"]):
        search_type  =  "rag"
    elif len(q.split()) < 3 :
        search_type = "clarify"

    state["search_type"] = search_type

    return state    

def router(state: RAGState):
    return state["search_type"]      

graph = StateGraph(RAGState)                       

graph.add_node("decide_search", decide_search)

graph.add_node("calculator", calculator_node)
graph.add_node("calculator_answer", calculator_answer_node)

graph.add_node("pgvector", pgvector_node)
graph.add_node("pgvector_answer", pgvector_answer_node)

graph.add_node("clarify", clarify_node)

graph.set_entry_point("decide_search")

graph.add_edge("pgvector", "pgvector_answer")
graph.add_edge("pgvector_answer", END)

graph.add_edge("calculator", "calculator_answer")
graph.add_edge("calculator_answer", END)

graph.add_edge("clarify", END)


graph.add_conditional_edges(
    "decide_search",
    router,
    {
        "math" : "calculator",
        "rag" : "pgvector",
        "clarify" : "clarify",
        "direct" : END
    }
)

app = graph.compile()

# tel me joke
# RAG
# 5 + 2
# Explain cricket
result = app.invoke({
    "question" : "what is cricket, please explain ?",
    "documents" : [],
    "tool_result" : "",
    "answer" : ""
})

print(result["answer"])