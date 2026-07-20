# 6. Diamond Pattern

rows = 5

print("Diamond Pattern")

# Upper part
for i in range(1, rows + 1):
    for space in range(rows - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()

# Lower part
for i in range(rows - 1, 0, -1):
    for space in range(rows - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()

    # 7. Number Triangle

rows = 5

print("Number Triangle Pattern")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

    # 8. Alphabet Pattern

rows = 5

print("Alphabet Pattern")

for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()