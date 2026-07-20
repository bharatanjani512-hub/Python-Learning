# Recursion Notes

Recursion is a technique in which a function calls itself to solve a problem by breaking it into smaller, similar subproblems.

A recursive function must always include a **base case** to stop the recursion.

---

# Why Recursion?

Recursion is useful when a problem can be divided into smaller versions of itself.

Common applications include:

- Factorial calculation
- Fibonacci sequence
- Tree traversal
- Directory traversal
- Divide and Conquer algorithms

---

# Structure of a Recursive Function

Every recursive function has two parts:

1. Base Case
2. Recursive Call

### Syntax

```python
def function_name(parameters):
    if base_case:
        return value
    else:
        return function_name(smaller_problem)
```

---

# Base Case

The base case is the condition that stops the recursive calls.

### Example

```python
def countdown(n):
    if n == 0:
        print("Done!")
        return

    print(n)
    countdown(n - 1)

countdown(5)
```

Output

```
5
4
3
2
1
Done!
```

---

# Factorial using Recursion

The factorial of a number is:

```
5! = 5 × 4 × 3 × 2 × 1
```

### Example

```python
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output

```
120
```

---

# Fibonacci Series using Recursion

Each number is the sum of the previous two numbers.

```
0 1 1 2 3 5 8 13 ...
```

### Example

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(7):
    print(fibonacci(i))
```

Output

```
0
1
1
2
3
5
8
```

---

# Recursion vs Loop

| Recursion | Loop |
|-----------|------|
| Function calls itself | Repeats using loops |
| Needs a base case | Needs a stopping condition |
| Easier for recursive problems | Often faster and uses less memory |
| Uses call stack | Uses iteration |

---

# Advantages

- Makes code shorter.
- Easy to understand for recursive problems.
- Useful for trees and graphs.
- Breaks complex problems into simpler ones.

---

# Limitations

- Uses more memory because of the call stack.
- Can be slower than loops.
- Missing a base case leads to infinite recursion.
- Very deep recursion can cause a `RecursionError`.

---

# Key Notes

- Every recursive function must have a base case.
- Each recursive call should reduce the problem size.
- Infinite recursion occurs if the base case is missing.
- Recursion is widely used in algorithms and data structures.
- Choose recursion when it makes the solution clearer.

---

# Summary

| Concept | Purpose |
|---------|---------|
| Recursion | Function calls itself |
| Base Case | Stops recursion |
| Recursive Call | Solves a smaller problem |
| Factorial | Product of numbers |
| Fibonacci | Sum of previous two numbers |