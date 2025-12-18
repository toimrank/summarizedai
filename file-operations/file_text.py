import os

file=open("example.txt", "w")
file.write("Hello, how are you doing 123 !")
file.close()

file=open("example.txt", "r")
content=file.read()
print(content)
file.close()

file=open('example.txt', "a")
file.write("\nHope you are doing well!")
file.close()

print("======>>>>>>")

with open("example.txt", "r") as file:
    #print(file.read())
    for line in file:
        print(line.strip())
        print("==== 1")

if os.path.exists("example.txt"):
    os.remove("example.txt")
