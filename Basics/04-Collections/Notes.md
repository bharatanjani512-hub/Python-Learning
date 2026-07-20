# Collections Notes

## Collections

Collections are special data structures used to store multiple values inside a single variable.

Python provides four built-in collection types:

- List
- Tuple
- Set
- Dictionary

---

# List

A List is an ordered and mutable collection.

### Features

- Ordered
- Mutable
- Allows duplicate values
- Indexed

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)
```

### Common Methods

```python
append()
insert()
remove()
pop()
sort()
reverse()
clear()
copy()
count()
index()
```

### Example

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)
```

---

# Tuple

A Tuple is an ordered but immutable collection.

### Features

- Ordered
- Immutable
- Allows duplicate values

### Example

```python
colors = ("Red", "Blue", "Green")

print(colors)
```

### Operations

```python
count()
index()
len()
```

---

# Set

A Set is an unordered collection of unique values.

### Features

- Unordered
- Mutable
- No duplicate values

### Example

```python
numbers = {1,2,3,4}

print(numbers)
```

### Common Methods

```python
add()
remove()
discard()
pop()
clear()
union()
intersection()
difference()
```

### Example

```python
numbers = {1,2,3}

numbers.add(4)

print(numbers)
```

---

# Dictionary

A Dictionary stores data in key-value pairs.

### Features

- Mutable
- Keys are unique
- Fast lookup

### Example

```python
student = {
    "name": "Anjani",
    "age": 22,
    "course": "Data Science"
}

print(student["name"])
```

### Common Methods

```python
keys()
values()
items()
get()
update()
pop()
clear()
```

### Example

```python
student = {
    "name": "Anjani"
}

student["age"] = 22

print(student)
```

---

# Comparison

| Collection | Ordered | Mutable | Duplicates |
|------------|---------|---------|------------|
| List | ✅ | ✅ | ✅ |
| Tuple | ✅ | ❌ | ✅ |
| Set | ❌ | ✅ | ❌ |
| Dictionary | ✅ | ✅ | Keys ❌ / Values ✅ |

---

# When to Use

### Use List

- Store ordered data
- Frequently modify items

### Use Tuple

- Store fixed data
- Protect data from modification

### Use Set

- Remove duplicates
- Perform mathematical set operations

### Use Dictionary

- Store key-value data
- Fast searching using keys

---

# Key Notes

- Lists are mutable.
- Tuples cannot be modified after creation.
- Sets automatically remove duplicates.
- Dictionaries use keys to access values.
- Collections improve code organization and efficiency.