# File Handling in Python

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, File Handling!")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:", content)
