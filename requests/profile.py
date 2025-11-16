import requests


cookies = {
    "session_id" : "21_session"
}

response = requests.get("http://127.0.0.1:8000/profile", cookies=cookies)
print(response.json())