import psycopg2
import openai
from langchain_text_splitters import CharacterTextSplitter


text = """
    LangChain is a framework that helps developers build applications powered by Large Language Models (LLMs). It provides tools to connect LLMs with external data, APIs, databases, and custom logic. LangChain’s core idea is chains—sequences of steps that structure how an LLM handles tasks. It also supports retrieval-augmented generation (RAG), allowing models to use your documents for accurate answers. With built-in components like prompt templates, text splitters, retrievers, memory, and agents, LangChain simplifies building chatbots, automation systems, and AI workflows. Overall, it makes LLM applications more reliable, scalable, and deeply integrated with real-world data and tools.
"""

conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="admin"
)

cursor = conn.cursor()

openai.api_key="<API_KEY>"

splitter = CharacterTextSplitter(
    separator=" ",
    chunk_size=200,
    chunk_overlap=30
)
 
def get_embeddings(text):
    response = openai.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks, 1):
    print(">>>>>>>>>>>>")
    print(chunk)
    emeddings = get_embeddings(text) 
    cursor.execute(
        """
        INSERT INTO document_content(description, embedding)
        VALUES(%s, %s)
        """,
        (chunk, emeddings)
    )

conn.commit()
cursor.close()
conn.close()

