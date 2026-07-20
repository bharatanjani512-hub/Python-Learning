# 10. Exception Handling 🐍

## 📖 Overview

Exception handling allows a program to detect and manage runtime errors gracefully, preventing unexpected crashes and improving program reliability.

---

## 🎯 Learning Objectives

After completing this topic I should be able to:

- Understand exceptions
- Use try and except blocks
- Use else and finally blocks
- Raise custom exceptions
- Handle multiple exceptions effectively

---

## 📚 Topics Covered

- Exceptions
- try Statement
- except Statement
- else Statement
- finally Statement
- raise Statement
- Custom Exceptions

---

## 💻 Example

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid number.")
```

---

## 🔑 Key Takeaways

- Exceptions prevent programs from crashing.
- `try` contains risky code.
- `except` handles errors.
- `finally` always executes.
- `raise` is used to generate custom exceptions.

---

## 📌 Status

✅ Completed