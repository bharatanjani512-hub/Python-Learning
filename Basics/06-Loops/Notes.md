# Loops Notes

Loops allow a block of code to execute repeatedly until a condition is met.

Python provides two main types of loops:

- for loop
- while loop

---

# for Loop

A **for loop** is used to iterate over a sequence like a list, string, tuple, or range.

### Syntax

```python
for variable in sequence:
    # code
```

### Example

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

# while Loop

A **while loop** repeats as long as the condition is true.

### Syntax

```python
while condition:
    # code
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# range() Function

The `range()` function generates a sequence of numbers.

### Examples

```python
range(5)

range(1, 6)

range(1, 11, 2)
```

### Example

```python
for i in range(1, 6):
    print(i)
```

---

# Nested Loops

A loop inside another loop is called a nested loop.

### Example

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

# break Statement

The `break` statement immediately terminates the loop.

### Example

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

---

# continue Statement

The `continue` statement skips the current iteration.

### Example

```python
for i in range(6):

    if i == 3:
        continue

    print(i)
```

---

# pass Statement

The `pass` statement does nothing. It acts as a placeholder.

### Example

```python
for i in range(5):

    if i == 3:
        pass

    print(i)
```

---

# Pattern Printing

Loops are commonly used to create patterns.

### Example

```python
for i in range(5):

    for j in range(i + 1):
        print("*", end="")

    print()
```

Output

```
*
**
***
****
*****
```

---

# Infinite Loop

A loop without a stopping condition runs forever.

### Example

```python
while True:
    print("Running...")
```

---

# Key Notes

- Loops reduce repetitive code.
- Use `for` when the number of iterations is known.
- Use `while` when the stopping condition is unknown.
- `break` exits the loop.
- `continue` skips an iteration.
- `pass` is a placeholder.
- Nested loops are useful for matrices and pattern problems.
- Avoid infinite loops unless intentionally required.

---

# Summary

| Concept | Purpose |
|---------|---------|
| for | Iterate over sequences |
| while | Repeat while a condition is true |
| range() | Generate numbers |
| break | Exit the loop |
| continue | Skip an iteration |
| pass | Placeholder |
| Nested Loop | Loop inside another loop |