import requests

user_id = 21

response = requests.get(f"http://127.0.0.1:8000/user/{user_id}")
user = response.json()
print(user)
print(user['id'])
print(user['name'])

