
---

### 4. Notes.md Template

````md
# Strings Notes

## String

A string is a sequence of characters enclosed in single, double, or triple quotes.

### Example

```python
name = "Python"
## String
---

## Indexing

Indexing is used to access individual characters in a string.

Python starts counting from **0**.

### Example

```python
name = "Python"

print(name[0])   # P
print(name[3])   # h
print(name[-1])  # n
```

---

## Slicing

Slicing extracts a portion of a string.

### Example

```python
name = "Python"

print(name[0:4])
print(name[2:])
print(name[:3])
```

---

## String Methods

Some commonly used methods:

```python
upper()
lower()
replace()
split()
strip()
find()
count()
```

### Example

```python
name = "python"

print(name.upper())
print(name.replace("python", "Java"))
```

---

## String Formatting

Python provides f-strings for formatting.

### Example

```python
name = "Anjani"

print(f"Hello {name}")
```

---

## Key Notes

- Strings are immutable.
- Index starts from 0.
- Negative indexing starts from the last character.