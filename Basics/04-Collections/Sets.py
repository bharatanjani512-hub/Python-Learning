my_set = {11, 12, 13, 14, 15}

print("Original Set:", my_set)

# Add element
my_set.add(16)
print("After Add:", my_set)

# Remove element
my_set.remove(13)
print("After Remove:", my_set)

# Union and Intersection
set2 = {14, 15, 16, 17}

print("Union:", my_set.union(set2))
print("Intersection:", my_set.intersection(set2))