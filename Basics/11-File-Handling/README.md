# 11. File Handling 🐍

## 📖 Overview

File handling allows Python programs to create, read, write, append, and manage files stored on a computer. It is essential for saving data permanently and working with external files.

---

## 🎯 Learning Objectives

After completing this topic I should be able to:

- Open files in different modes
- Read data from files
- Write data to files
- Append data to existing files
- Use the `with` statement
- Handle files safely and efficiently

---

## 📚 Topics Covered

- Opening Files
- File Modes
- Reading Files
- Writing Files
- Appending Files
- Closing Files
- with Statement

---

## 💻 Example

```python
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

---

## 🔑 Key Takeaways

- `open()` is used to open files.
- Always close files after use.
- The `with` statement automatically closes files.
- Different modes are used for reading, writing, and appending.

---

## 📌 Status

✅ Completed