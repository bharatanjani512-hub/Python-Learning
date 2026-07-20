# 1. Square Pattern

rows = 5

print("Square Pattern")

for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()

    # 2. Right Triangle Pattern

rows = 5

print("Right Triangle Pattern")

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

    # 3. Inverted Right Triangle Pattern

rows = 5

print("Inverted Right Triangle Pattern")

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

    # 4. Pyramid Pattern

rows = 5

print("Pyramid Pattern")

for i in range(1, rows + 1):
    for space in range(rows - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()

    # 5. Inverted Pyramid Pattern

rows = 5

print("Inverted Pyramid Pattern")

for i in range(rows, 0, -1):
    for space in range(rows - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()