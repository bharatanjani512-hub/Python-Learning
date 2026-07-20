# Advanced Concepts Notes

Advanced Python concepts help developers write efficient, reusable, and maintainable programs. These features are commonly used in professional software development.

---

# Modules

A **module** is a Python file containing functions, variables, or classes that can be imported into another program.

### Example

```python
import math

print(math.sqrt(25))
```

---

# Packages

A **package** is a collection of related Python modules organized in directories.

Example:

```
project/
│
├── package/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
```

Importing from a package:

```python
from package import module1
```

---

# pip

`pip` is Python's package manager used to install, update, and remove third-party libraries.

### Common Commands

Install a package

```bash
pip install numpy
```

Upgrade a package

```bash
pip install --upgrade pandas
```

Uninstall a package

```bash
pip uninstall numpy
```

View installed packages

```bash
pip list
```

---

# Virtual Environment

A virtual environment creates an isolated Python environment for a project, preventing dependency conflicts.

### Create a virtual environment

```bash
python -m venv myenv
```

### Activate (Windows)

```bash
myenv\Scripts\activate
```

### Activate (macOS/Linux)

```bash
source myenv/bin/activate
```

### Deactivate

```bash
deactivate
```

---

# Iterators

An iterator is an object that allows sequential traversal of elements.

### Example

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

---

# Generators

Generators produce values one at a time using the `yield` keyword, making them memory-efficient.

### Example

```python
def countdown(n):

    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
```

---

# Decorators

Decorators modify the behavior of a function without changing its original code.

### Example

```python
def welcome(func):

    def wrapper():
        print("Welcome")
        func()

    return wrapper

@welcome
def greet():
    print("Hello!")

greet()
```

---

# Iterator vs Generator

| Iterator | Generator |
|----------|-----------|
| Uses `iter()` and `next()` | Uses `yield` |
| More code to implement | Easier to write |
| Stores state manually | Automatically maintains state |
| Can consume more memory | Memory efficient |

---

# Advantages

- Encourages modular programming.
- Makes code reusable.
- Improves project organization.
- Reduces memory usage with generators.
- Simplifies code using decorators.

---

# Key Notes

- A module is a single Python file.
- A package is a collection of modules.
- `pip` manages third-party libraries.
- Virtual environments isolate project dependencies.
- Iterators traverse data one element at a time.
- Generators use `yield` for efficient iteration.
- Decorators enhance existing functions without modifying them.

---

# Summary

| Concept | Purpose |
|---------|---------|
| Module | Reusable Python file |
| Package | Collection of modules |
| pip | Package manager |
| Virtual Environment | Isolated project environment |
| Iterator | Sequential data traversal |
| Generator | Memory-efficient iterator |
| Decorator | Modify function behavior |