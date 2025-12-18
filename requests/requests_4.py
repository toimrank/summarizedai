import requests

user_id=31

user = {
    "id": 31,
    "name": "Robotech",
    "age": 54,
    "city": "Phoenix",
    "password": "zxcvb"
}

response = requests.put(f"http://127.0.0.1:8000/user/{user_id}", json=user)
print(response.json())
