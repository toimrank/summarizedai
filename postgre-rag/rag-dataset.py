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

blog_data = [
    # 1: AI / ML
    ("Introduction to Machine Learning",
     "Machine learning allows computers to learn from data without being explicitly programmed. This post covers supervised, unsupervised, and reinforcement learning."),

    # 2: Databases / PostgreSQL
    ("Getting Started with PostgreSQL",
     "PostgreSQL is a powerful open-source relational database. Learn how to install it, set up databases, and perform basic CRUD operations."),

    # 3: AI / Vector Search
    ("Semantic Search with pgvector",
     "Learn how to implement semantic search using pgvector in PostgreSQL, combining embeddings from OpenAI to retrieve contextually relevant information."),

    # 4: Programming / Python
    ("Python Tips for Beginners",
     "This post shares practical tips for writing clean, efficient Python code, including list comprehensions, lambda functions, and virtual environments."),

    # 5: Web Development / JavaScript
    ("Modern JavaScript Features",
     "Explore ES6+ features like arrow functions, template literals, destructuring, and modules to write modern, maintainable JavaScript code."),

    # 6: Cloud Computing / AWS
    ("Introduction to AWS Lambda",
     "AWS Lambda lets you run code without provisioning servers. Learn about serverless functions, triggers, and deployment best practices."),

    # 7: Cybersecurity
    ("Basic Cybersecurity Practices",
     "Understand the fundamentals of cybersecurity, including strong passwords, two-factor authentication, firewalls, and regular updates."),

    # 8: DevOps / CI-CD
    ("CI/CD with GitHub Actions",
     "Learn how to automate your build, test, and deployment pipelines using GitHub Actions for faster and reliable software delivery."),

    # 9: Data Science / Pandas
    ("Data Analysis with Pandas",
     "Pandas is a Python library for data manipulation and analysis. Learn to work with DataFrames, perform groupby operations, and visualize data."),

    # 10: AI / RAG / LLM
    ("Building a Chatbot with Retrieval-Augmented Generation",
     "Combine vector databases and LLMs to build a chatbot that provides contextually accurate answers by retrieving relevant documents from your knowledge base.")
]

for title, content in blog_data:

    combined_text = f"Title: {title}\n Content: {content}"

    emb = clinet.embeddings.create(
        model="text-embedding-3-small",
        input=combined_text
    ).data[0].embedding

    cur.execute("""
        INSERT INTO blog_posts (title, content, embedding)
        VALUES (%s, %s, %s);
        """, (title, content, emb))
    
    print(f"Inserted blog: {title}")

conn.commit()
cur.close()
conn.close()