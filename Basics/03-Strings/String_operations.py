# String Operations Program

# Taking input
text = input("Enter a string: ")

# Check Substring
sub = input("Enter substring to check: ")
if sub in text:
    print("Substring found")
else:
    print("Substring not found")

# Concatenation
concat = text + " - Python"
print("Concatenation:", concat)

# Repetition
print("Repetition:", text * 2)

# Remove Spaces
no_spaces = text.replace(" ", "")
print("Without spaces:", no_spaces)

# Split String
split_text = text.split()
print("Split string:", split_text)

# Join String
joined_text = "-".join(split_text)
print("Joined string:", joined_text)

# Find Operation
print("Find 'a':", text.find("a"))

# Length of String
print("Length of string:", len(text))

# Convert to Uppercase
print("Uppercase:", text.upper())

# Convert to Lowercase
print("Lowercase:", text.lower())

# Access First Character
if len(text) > 0:
    print("First character:", text[0])

# Slicing
print("Slicing (first 3 characters):", text[:3])

# Replace Word
replaced_text = text.replace("Python", "Java")
print("After replace:", replaced_text)

# Find Position
print("Position of substring:", text.find(sub))

# Count Occurrences
print("Count of substring:", text.count(sub))
