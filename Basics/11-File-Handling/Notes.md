# File Handling Notes

File handling allows Python programs to store, retrieve, and manipulate data stored in files. Unlike variables, data stored in files remains available even after the program ends.

---

# Why File Handling?

File handling helps us:

- Store data permanently
- Read existing data
- Write new data
- Update files
- Process large amounts of information

---

# Opening a File

The `open()` function is used to open a file.

### Syntax

```python
file = open("filename.txt", "mode")
```

### Example

```python
file = open("sample.txt", "r")
print(file.read())
file.close()
```

---

# File Modes

| Mode | Description |
|------|-------------|
| `r` | Read (default) |
| `w` | Write (creates or overwrites file) |
| `a` | Append data |
| `x` | Create a new file |
| `rb` | Read binary file |
| `wb` | Write binary file |

---

# Reading Files

### read()

Reads the entire file.

```python
file = open("sample.txt", "r")

print(file.read())

file.close()
```

---

### readline()

Reads one line at a time.

```python
file = open("sample.txt", "r")

print(file.readline())

file.close()
```

---

### readlines()

Reads all lines into a list.

```python
file = open("sample.txt", "r")

print(file.readlines())

file.close()
```

---

# Writing Files

The `w` mode creates a new file or overwrites an existing one.

```python
file = open("sample.txt", "w")

file.write("Hello Python!")

file.close()
```

---

# Appending Files

The `a` mode adds data to the end of a file.

```python
file = open("sample.txt", "a")

file.write("\nWelcome to File Handling")

file.close()
```

---

# Closing Files

Always close a file after completing operations.

```python
file.close()
```

Closing files helps release system resources.

---

# Using the with Statement

The `with` statement automatically closes the file after the block of code finishes.

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

This is the recommended way to work with files.

---

# Real-world Example

Saving student information to a file.

```python
with open("students.txt", "a") as file:
    file.write("Anjani, Data Science\n")
```

Reading the file:

```python
with open("students.txt", "r") as file:
    print(file.read())
```

---

# Advantages of File Handling

- Permanent data storage
- Easy data sharing
- Efficient data processing
- Supports text and binary files

---

# Key Notes

- Use `open()` to access files.
- Always specify the correct file mode.
- Prefer the `with` statement for automatic file closing.
- `w` overwrites existing content.
- `a` adds data without removing existing content.
- Reading large files line by line is more memory-efficient.

---

# Summary

| Concept | Purpose |
|---------|---------|
| `open()` | Opens a file |
| `read()` | Reads entire file |
| `readline()` | Reads one line |
| `readlines()` | Reads all lines |
| `write()` | Writes data |
| `append()` | Adds data to a file |
| `close()` | Closes the file |
| `with` | Automatically manages file closing |