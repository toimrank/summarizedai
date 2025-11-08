from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

api_key = "<API_KEY>"

llm = OpenAI(model="gpt-4o-mini", api_key=api_key)

prompt = PromptTemplate.from_template("Explain Python in one line.")
final_prompt = prompt.format(topic="Artificial Intelligence")

response = llm.invoke(final_prompt)
print(response.content)
