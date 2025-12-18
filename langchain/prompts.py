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

# Format the prompt with dynamic values
messages = prompt.format(
    example_topic="Machine Learning",
    topic="LangChain Prompt Template",
    level="beginner"
)

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo", 
    temperature=0, 
    api_key="<API_KEY>"
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    google_api_key="<API_KEY>"
)

# call the model
response = llm.invoke(messages)

print(response)