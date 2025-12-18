from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage

@tool
def search_products(keyword: str):
    """Search for products by keyword"""
    products = {
        "laptop": [
            {"name": "Dell Inspiron", "price": 700},
            {"name": "MacBook Air", "price": 1200},
        ],
        "phone": [
            {"name": "iPhone 15", "price": 999},
            {"name": "Samsung S23", "price": 899},
        ]
    }
    return products.get(keyword.lower(), "No Product Found!")

@tool
def apply_discount(price: float, percent: float):
    """Apply discount percent to price"""
    discounted = price - (price * percent / 100)
    return round(discounted, 2)

llm = ChatOpenAI(
    model="gpt-4.1",
    api_key="<API_KEY>"    
)

agent = create_agent(
    llm,
    tools=[search_products, apply_discount]
)

result = agent.invoke({
    "messages" :[
        HumanMessage(
            content="Find me the cheapest laptop"
        )
    ]
})

messages = result.get("messages",[])
ai_message_content = None

for msg in messages:
    if msg.__class__.__name__ == "AIMessage" and msg.content:
        ai_message_content = msg.content
        break

print(ai_message_content)