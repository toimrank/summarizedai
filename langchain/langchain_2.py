from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts.prompt import PromptTemplate

# 1️⃣ Hardcode your Google API key
api_key = "<API_KEY>"  # replace with your real key

# 2️⃣ Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  # pick the model you have access to
    api_key=api_key,
)

prompt = PromptTemplate.from_template("Explain Python in one line.")
final_prompt = prompt.format(topic="Artificial Intelligence")

response = llm.invoke(final_prompt)
print(response.content)