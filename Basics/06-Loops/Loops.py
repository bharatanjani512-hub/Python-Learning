# 1. Print even numbers between 1 and 50
print("1. Even numbers (1 to 50)")
for i in range(2, 51, 2):
    print(i, end=" ")
print("\n")

# 2. Reverse counting from 20 to 1
print("2. Reverse counting (20 to 1)")
for a in range(20, 0, -1):
    print(a, end=" ")
print("\n")

# 3. Sum of first 10 natural numbers
print("3. Sum of first 10 natural numbers")
total = 0
for b in range(1, 11):
    total += b
    print(b, end=" ")
print("\nSum =", total)
print()

# 4. Count vowels in a given string
print("4. Vowels count")
s = "Anjani"
count = 0

for n in s:
    if n in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)
print()

# 5. Numbers divisible by 5 between 1 to 100
print("5. Numbers divisible by 5 (1-100)")
for y in range(5, 101, 5):
    print(y, end=" ")
print()