import requests

response = requests.get("http://127.0.0.1:8000/users")
json_reponse = response.json()
for user in json_reponse:
    print(user)

