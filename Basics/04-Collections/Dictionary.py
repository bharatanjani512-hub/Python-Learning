my_dict = {
    "name": "Anjani",
    "age": 22,
    "course": "MSc Data Science"
}

print("Original Dictionary:", my_dict)

# Access value
print("Name:", my_dict["name"])

# Add new key-value pair
my_dict["city"] = "Dharamshala"
print("After Adding City:", my_dict)

# Update value
my_dict["age"] = 22
print("After Updating Age:", my_dict)

# Remove key
my_dict.pop("course")
print("After Removing Course:", my_dict)

# Display keys and values
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())