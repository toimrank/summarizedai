import sqlite3
from typing import TypedDict, List

from langchain.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END

DB_NAME = "practice.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_message(role: str, content: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO messages (role, content) VALUES(?, ?)",
        (role, content)
    )
    conn.commit()
    conn.close()

def load_message():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT role, content FROM messages")
    rows = cursor.fetchall()

    conn.close()

    messages = []
    for role, content in rows:
        if role == "user":
            messages.append(HumanMessage(content=content))
        else:
            messages.append(AIMessage(content=content))    

    return messages

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="<API_KEY>"
)

class ChatState(TypedDict):
    user_input: str
    messages: List

def load_history(state: ChatState):
    history = load_message()
    return {
        "messages" : history + [HumanMessage(content=state["user_input"])]
    }

def chat_node(state: ChatState):
    response = llm.invoke(state["messages"])
    return {
        "messages" : state["messages"] + [response] 
    }

def save_to_db(state: ChatState):
    last_user = state["messages"][-2]
    last_ai = state["messages"][-1]

    save_message("user", last_user.content)
    save_message("assistant", last_ai.content)

    return state

graph = StateGraph(ChatState)

graph.add_node("load_history", load_history)
graph.add_node("chat", chat_node)
graph.add_node("save", save_to_db)

graph.add_edge(START, "load_history")
graph.add_edge("load_history", "chat")
graph.add_edge("chat", "save")
graph.add_edge("save", END)

chatbot = graph.compile()
print("SQLite + LangGraph Chatbot (type 'Exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    result = chatbot.invoke({
        "user_input" : user_input
    })

    ai_meesage = result["messages"][-1]
    print("Bot: ", ai_meesage.content)
