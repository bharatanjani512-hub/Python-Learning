print("1. Even/Odd")
print("2. Largest among three numbers")
print("3. Positive/Negative/Zero")

choice = int(input("Enter your choice (1-3): "))

# Even or Odd
if choice == 1:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

# Largest among three numbers
elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if a >= b and a >= c:
        print("Largest number is:", a)
    elif b >= a and b >= c:
        print("Largest number is:", b)
    else:
        print("Largest number is:", c)

# Positive, Negative or Zero
elif choice == 3:
    n = int(input("Enter a number: "))

    if n > 0:
        print("Positive number")
    elif n < 0:
        print("Negative number")
    else:
        print("Zero")

else:
    print("Invalid choice")