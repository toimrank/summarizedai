import requests

cookies = {
    "session_id" : "21_session"
}

response = requests.post(f"http://127.0.0.1:8000/logout",cookies=cookies)
print(response.json())