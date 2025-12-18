import pandas as pd

data = {
    "Name" : ["Mike","Bob","Charlie"],
    "Age" : [331,34,67],
    "City" : ["Austin","Phoenix","Chicago"]
}

df = pd.DataFrame(data)

file_name = "data.xlsx"

with open(file_name, "wb") as file:
    df.to_excel(file, index=False)

with open(file_name, "rb") as file:
    df = pd.read_excel(file)
    print(df)    