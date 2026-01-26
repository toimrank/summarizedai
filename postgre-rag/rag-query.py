from openai import OpenAI
import psycopg2

clinet = OpenAI(api_key="<API_KEY>")

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="admin",
    host="localhost"
)

cur = conn.cursor()

query_text = "How to do data analysis in Python ?"

query_emb = clinet.embeddings.create(
        model="text-embedding-3-small",
        input=query_text
    ).data[0].embedding

# 3️⃣ Perform semantic search in pgvector
cur.execute("""
    SELECT content
    FROM blog_posts
    ORDER BY embedding <-> %s::vector
    LIMIT 1;
""", (query_emb,))

result = cur.fetchone()
print("Answer:", result[0])