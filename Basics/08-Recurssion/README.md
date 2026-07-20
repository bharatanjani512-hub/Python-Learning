# 08. Recursion 🐍

## 📖 Overview

Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem. It is commonly used in mathematical computations, tree traversals, searching algorithms, and divide-and-conquer techniques.

---

## 🎯 Learning Objectives

After completing this topic I should be able to:

- Understand recursion
- Identify the base case
- Write recursive functions
- Solve problems using recursion
- Compare recursion with loops

---

## 📚 Topics Covered

- Recursion
- Base Case
- Recursive Call
- Factorial using Recursion
- Fibonacci Series
- Advantages and Limitations

---

## 💻 Example

```python
def countdown(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
```

---

## 🔑 Key Takeaways

- Every recursive function must have a base case.
- Recursive calls solve a smaller version of the same problem.
- Missing a base case can cause infinite recursion.
- Recursion is elegant but may use more memory than loops.

---

## 📌 Status

✅ Completed