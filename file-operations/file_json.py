import json

data = {
    "name" : "Mike",
    "age" : 28,
    "skills" : ["Python", "Streamlit", "Langchain"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    data = json.load(file)
    print(data) 
    print("Name:", data["name"])    