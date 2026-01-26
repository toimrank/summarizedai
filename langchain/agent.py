from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import  Tool

def calculator_tool(query: str) -> str:
    try:
        return str(eval(query))
    except Exception:
        return "Invalid calculation"

tool = Tool(
    name="Calculator",
    func=calculator_tool,
    description="Performs basic math calculations like '2 + 2' or '10 * 5'"
)
tools = [tool]

llm = ChatOpenAI(
    model="gpt-4o-mini", 
    temperature=0,
    api_key="<API_KEY>"
)

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful weather assistant. Use the provided tool when needed."
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Calculate 25 * 4"}]
})

print(result["messages"][-1].content)