# Sum of n natural numbers
print("1. Sum of n natural numbers")
n = int(input("Enter number: "))
i = 1
s = 0
while i <= n:
    s += i
    i += 1
print(s)

# Even numbers upto n 
print("2. Even numbers upto n ")
n = int(input("Enter number: "))
i = 2
while i <= n:
    print(i)
    i += 2

# Factorial of a number
print("3. Factorial of a number")

n = int(input("Enter number: "))
fact = 1
while n > 0:
    fact *= n
    n -= 1
print(fact)