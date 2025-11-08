with open("victor.jpg", "rb") as img_file:
    data = img_file.read()

with open("victor_binary.bin", "wb") as file:
    file.write(data) 

with open("victor_binary.bin", "rb") as file:
    binary_content = file.read()        

with open("victor_1.jpg", "wb") as file:
    file.write(binary_content)     