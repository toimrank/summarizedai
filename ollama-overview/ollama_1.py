import ollama

response=ollama.chat(
    model="gemma3",
    messages=[{
        "role" : "user",
        "content" : "Explain Python in one line."
    }]
)

print(response["message"]["content"])