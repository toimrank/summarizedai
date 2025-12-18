from langchain_postgres import PGVector
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key="<API_KEY>"
)

connection = "postgresql+psycopg://postgres:admin@localhost:5432/postgres"

vector_store = PGVector(
    embeddings=embeddings,
    collection_name="document_content",
    connection=connection,
    use_jsonb=True
)

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={'k' : 3}
)


prompt = ChatPromptTemplate.from_template("""
    You are a helpful AI assistant.
    Use ONLY the context below to answer the question.
    If the answer is not in the context, say "I don't know".

    Context:
    {context}

    Question:
    {question}
""")

parser = StrOutputParser()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="<API_KEY>"
)

chain = (
    {
        "context" : retriever,
        "question" : RunnablePassthrough()
    }
    | prompt
    | llm
    | parser
)


response = chain.invoke("What is Langchain ?")
print(response)