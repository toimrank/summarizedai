import requests

user_id=21
password="asd123"

response = requests.post(f"http://127.0.0.1:8000/login?user_id={user_id}&password={password}")
print(response.json())