# Functions Notes

Functions are reusable blocks of code that perform a specific task.

They help avoid repetition and make programs easier to understand and maintain.

---

# Why Functions?

Functions help us:

- Reuse code
- Improve readability
- Reduce duplication
- Organize large programs

---

# Built-in Functions

Python provides many built-in functions.

Examples:

```python
print()
len()
type()
input()
range()
sum()
max()
min()
```

Example

```python
numbers = [10, 20, 30]

print(len(numbers))
print(sum(numbers))
```

---

# User-defined Functions

Users can create their own functions using the `def` keyword.

### Syntax

```python
def function_name():
    # code
```

### Example

```python
def greet():
    print("Welcome to Python!")

greet()
```

---

# Parameters and Arguments

### Parameters

Variables defined inside the function definition.

### Arguments

Actual values passed to the function.

Example

```python
def greet(name):
    print("Hello", name)

greet("Anjani")
```

Here,

Parameter → `name`

Argument → `"Anjani"`

---

# Return Statement

The `return` keyword sends a value back to the caller.

Example

```python
def add(a, b):
    return a + b

result = add(10, 5)

print(result)
```

---

# Default Parameters

A function can have default parameter values.

Example

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Anjani")
```

---

# Lambda Functions

Lambda functions are anonymous one-line functions.

### Syntax

```python
lambda arguments: expression
```

### Example

```python
square = lambda x: x * x

print(square(5))
```

---

# Scope

Variables created inside a function are local variables.

Example

```python
def test():
    x = 10
    print(x)

test()
```

---

# Key Notes

- Functions improve code reusability.
- Parameters receive values.
- Arguments provide values.
- Return sends output back.
- Lambda functions are useful for short operations.
- Built-in functions save development time.

---

# Summary

| Concept | Purpose |
|---------|---------|
| Built-in Function | Provided by Python |
| User-defined Function | Created by the programmer |
| Parameter | Variable in function definition |
| Argument | Actual value passed |
| Return | Sends value back |
| Lambda | Anonymous function |