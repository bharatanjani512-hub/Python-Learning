# Conditional Statements Notes

Conditional statements allow a program to make decisions based on conditions. The program executes different blocks of code depending on whether a condition is **True** or **False**.

---

# if Statement

The `if` statement executes a block of code only when the specified condition is true.

### Syntax

```python
if condition:
    # code
```

### Example

```python
age = 20

if age >= 18:
    print("You are an Adult.")
```

---

# if-else Statement

The `if-else` statement provides an alternative block of code when the condition is false.

### Syntax

```python
if condition:
    # code
else:
    # code
```

### Example

```python
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

---

# elif Statement

The `elif` (else if) statement checks multiple conditions. Once a condition is true, the remaining conditions are skipped.

### Syntax

```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

### Example

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

---

# Nested if Statement

A nested `if` is an `if` statement inside another `if` statement.

### Example

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Underage")
```

---

# Logical Operators

Logical operators combine multiple conditions.

### AND Operator (`and`)

Returns **True** only if both conditions are true.

```python
age = 22
student = True

if age > 18 and student:
    print("Eligible for student discount")
```

---

### OR Operator (`or`)

Returns **True** if at least one condition is true.

```python
marks = 85
sports = True

if marks > 90 or sports:
    print("Eligible for scholarship")
```

---

### NOT Operator (`not`)

Reverses the result of a condition.

```python
logged_in = False

if not logged_in:
    print("Please log in")
```

---

# Comparison Operators

Conditional statements commonly use comparison operators.

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

# Real-world Example

```python
username = "Anjani"
password = "python123"

if username == "Anjani" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")
```

---

# Key Notes

- Conditional statements control the flow of a program.
- Python uses indentation instead of braces `{}`.
- Conditions always evaluate to **True** or **False**.
- `elif` is used to check multiple conditions efficiently.
- Nested `if` statements are useful for checking multiple levels of conditions.
- Logical operators (`and`, `or`, `not`) combine or modify conditions.
- Proper indentation is mandatory in Python.

---

# Summary

| Statement | Purpose |
|-----------|---------|
| `if` | Executes code if a condition is true |
| `if-else` | Chooses between two blocks of code |
| `elif` | Checks multiple conditions |
| Nested `if` | Places one `if` inside another |
| `and` | All conditions must be true |
| `or` | At least one condition must be true |
| `not` | Reverses the result of a condition |