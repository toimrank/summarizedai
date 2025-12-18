import json
from langchain_openai import ChatOpenAI

# Create dynamic prompts with variables.
from langchain_core.prompts import ChatPromptTemplate

# Parse and process the output from the language model.
from langchain_core.output_parsers import StrOutputParser

# Set the openai API key for authentication with OpenAI.
OPENAI_API_KEY = "<API_KEY>"

topic = "india"

# Initialize the LLM chat model. Here, we can declare other chat 
# models also like Anthropic, Azure, Google Geminin, AWS, Groq, etc.
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini")

# Process or parse the output returned clean, usable string format by a language model
parser = StrOutputParser()

# Chain 1: This is to create prompy..Summarize prompt
summary_prompt = ChatPromptTemplate.from_template("Summarize the topic: {topic}")

# connects different components (like prompts, language models, 
# and output parsers) into a single pipeline.
summary_chain = summary_prompt | llm | parser

# Step 1: Get summary
summary = summary_chain.invoke({"topic": topic})

print(summary)
print("==========>>>>>>>>>>>>>")

# Chain 2: Country identification prompt
points_prompt = ChatPromptTemplate.from_template(
    "Convert {summary} in to three short points."
)


points_chain = points_prompt | llm | parser

# Step 2: Generate country name from summary
points = points_chain.invoke({"summary": summary})

print(points)