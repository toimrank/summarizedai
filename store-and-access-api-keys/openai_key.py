from openai import OpenAI
import yaml
import os

# First way
#api_key = "<API_KEY>"

# second way
# Load config.yaml
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
    print(config)
    print(config["openai"]["api_key"])
    api_key = config["openai"]["api_key"]

# Third way
print("=============")
print(os.getenv("OPENAI_API_KEY"))
api_key = os.getenv("OPENAI_API_KEY")

print(os.getenv("MY_VARIABLE"))


# Create an OpenAI client
client = OpenAI()

# Send a chat message
response = client.chat.completions.create(
    model="gpt-4o-mini",  # or "gpt-4o", "gpt-3.5-turbo"
    messages=[
        {"role": "user", "content": "Hello! How are you today?"}
    ]
)

# Print the AI's reply
print(response.choices[0].message.content)