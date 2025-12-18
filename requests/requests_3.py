import requests

user = {
    "id": 31,
    "name": "Robo",
    "age": 45,
    "city": "Chicago",
    "password": "qwerty"
}

response = requests.post(f"http://127.0.0.1:8000/user", json=user)
print(response)
