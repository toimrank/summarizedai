from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

prompt = ChatPromptTemplate([
    
    # System instruction
    ("system", 
     "You are an expert AI tutor. "
     "Explain concepts clearly with simple examples."),

    # Few-shot example (Human → AI)
    ("human", "Explain {example_topic} in simple terms."),
    ("ai", 
     "{example_topic} is a basic concept where we break complex ideas "
     "into smaller, understandable parts using real-life examples."),

    # Actual user input (dynamic)
    ("human", 
     "Explain {topic} for a {level} learner.")

])

messages = prompt.format(
    example_topic="Machine learning",
    topic="Langchain",
    level="beginner"
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key="<API_KEY>"
)

response = llm.invoke(messages)
print(response.content)