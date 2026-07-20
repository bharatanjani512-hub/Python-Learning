# Program to implement user-defined functions in Python


def find_sum(a, b):
    return a + b


def find_square(n):
    return n * n


def multiply(a, b):
    return a * b


print("===== User Defined Functions in Python =====")

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


add = find_sum(num1, num2)
print("Sum of", num1, "and", num2, "is:", add)


sq = find_square(num1)
print("Square of", num1, "is:", sq)


m1 = multiply(num1, num2)
print("Multiplication of", num1, "and", num2, "is:", m1)