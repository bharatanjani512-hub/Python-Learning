# Create and write file
file = open("sample.txt", "w")
file.write("Hello, this is file handling example.\n")
file.close()

# Read file
file = open("sample.txt", "r")
print("File content:")
print(file.read())
file.close()

# Append data
file = open("sample.txt", "a")
file.write("This is appended text.\n")
file.close()

# Read again
file = open("sample.txt", "r")
print("Updated content:")
print(file.read())
file.close()