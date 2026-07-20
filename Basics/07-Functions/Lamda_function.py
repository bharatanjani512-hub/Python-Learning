data = [1, 2, 3, 4, 5]

square = list(map(lambda x: x**2, data))
print("Squares:", square)

even = list(filter(lambda x: x % 2 == 0, data))
print("Even numbers:", even)