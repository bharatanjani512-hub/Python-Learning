# Program to demonstrate built-in functions in Python

print("===== Built-in Functions in Python =====")

# 1. print()
print("\n1. print() Function:")
print("Hello, Welcome to Python!")

# 2. input()
print("\n2. input() Function:")
name = input("Enter your name: ")
print("Your name is:", name)

# 3. len()
print("\n3. len() Function:")
text = "Python Programming"
print("Length of string is:", len(text))

# 4. type()
print("\n4. type() Function:")
x = 100
print("Type of x is:", type(x))

# 5. int()
print("\n5. int() Function:")
a = "25"
print("String converted to integer:", int(a))

# 6. float()
print("\n6. float() Function:")
b = "12.5"
print("String converted to float:", float(b))

# 7. str()
print("\n7. str() Function:")
num = 500
print("Number converted to string:", str(num))

# 8. sum()
print("\n8. sum() Function:")
numbers = [10, 20, 30, 40]
print("Sum of list elements is:", sum(numbers))

# 9. max()
print("\n9. max() Function:")
print("Maximum value is:", max(numbers))

# 10. min()
print("\n10. min() Function:")
print("Minimum value is:", min(numbers))

# 11. abs()
print("\n11. abs() Function:")
print("Absolute value of -15 is:", abs(-15))

# 12. round()
print("\n12. round() Function:")
print("Rounded value of 3.67 is:", round(3.67))
print("Rounded value of 3.678 to 2 decimal places is:", round(3.678, 2))

# 13. sorted()
print("\n13. sorted() Function:")
nums = [50, 10, 40, 20, 30]
print("Sorted list is:", sorted(nums))

# 14. range()
print("\n14. range() Function:")
print("Numbers from 0 to 4 are:")
for i in range(5):
    print(i, end=" ")

# 15. list()
print("\n\n15. list() Function:")
t = (1, 2, 3, 4)
print("Tuple converted to list:", list(t))

# 16. tuple()
print("\n16. tuple() Function:")
l = [5, 6, 7, 8]
print("List converted to tuple:", tuple(l))

# 17. set()
print("\n17. set() Function:")
duplicate_list = [1, 2, 2, 3, 3, 4]
print("Set after removing duplicates:", set(duplicate_list))

# 18. pow()
print("\n18. pow() Function:")
print("2 raised to power 3 is:", pow(2, 3))

# 19. id()
print("\n19. id() Function:")
y = 10
print("Memory address of y is:", id(y))
quit()
