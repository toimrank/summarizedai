import requests

user_id=31

response = requests.delete(f"http://127.0.0.1:8000/user/{user_id}")
print(response)
