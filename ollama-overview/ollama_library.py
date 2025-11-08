import requests

url = "http://127.0.0.1:11434/v1/completions"

body={
    "model": "gemma3",
    "prompt": "What is python in one line",
    "max_tokens": 300
}

response=requests.post(url, json=body)

response_json = response.json()

print(response_json["choices"][0]["text"])