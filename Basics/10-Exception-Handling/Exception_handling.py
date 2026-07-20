try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

except ValueError:
    print("Error: Invalid input")

else:
    print("Result:", result)

finally:
    print("Exception completed")