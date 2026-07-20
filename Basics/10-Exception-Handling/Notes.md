# Exception Handling Notes

Exception handling is used to detect and handle runtime errors so that a program continues to execute instead of terminating unexpectedly.

Python uses the `try`, `except`, `else`, and `finally` blocks for exception handling.

---

# What is an Exception?

An exception is an error that occurs during program execution.

Common exceptions include:

- ZeroDivisionError
- ValueError
- TypeError
- IndexError
- KeyError
- FileNotFoundError

---

# try Statement

The `try` block contains code that might generate an exception.

### Syntax

```python
try:
    # risky code
```

### Example

```python
try:
    num = int(input("Enter a number: "))
    print(num)
```

---

# except Statement

The `except` block executes if an exception occurs.

### Syntax

```python
try:
    # code
except ExceptionType:
    # handling code
```

### Example

```python
try:
    num = 10 / 0

except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

---

# Handling Multiple Exceptions

Multiple exceptions can be handled separately.

### Example

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# else Statement

The `else` block executes only if no exception occurs.

### Example

```python
try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid Input")

else:
    print("You entered:", num)
```

---

# finally Statement

The `finally` block always executes, whether an exception occurs or not.

### Example

```python
try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program Finished")
```

---

# raise Statement

The `raise` keyword is used to generate an exception manually.

### Example

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

---

# Custom Exceptions

Users can define their own exception classes.

### Example

```python
class InvalidAgeError(Exception):
    pass

age = -2

if age < 0:
    raise InvalidAgeError("Invalid age entered.")
```

---

# Common Exceptions

| Exception | Description |
|-----------|-------------|
| ValueError | Invalid value |
| TypeError | Wrong data type |
| ZeroDivisionError | Division by zero |
| IndexError | Invalid list index |
| KeyError | Missing dictionary key |
| FileNotFoundError | File does not exist |

---

# Real-world Example

```python
try:
    username = input("Username: ")
    password = input("Password: ")

    if password != "python123":
        raise ValueError("Incorrect password.")

    print("Login Successful")

except ValueError as error:
    print(error)

finally:
    print("Login Attempt Finished")
```

---

# Key Notes

- Exception handling prevents program crashes.
- Use `try` for risky code.
- Use `except` to handle errors.
- `else` executes only when no exception occurs.
- `finally` always executes.
- `raise` creates custom exceptions.
- Handle specific exceptions instead of using a generic `except`.

---

# Summary

| Concept | Purpose |
|---------|---------|
| try | Contains risky code |
| except | Handles exceptions |
| else | Executes if no exception occurs |
| finally | Always executes |
| raise | Creates an exception |
| Custom Exception | User-defined exception |