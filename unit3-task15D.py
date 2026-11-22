from functools import reduce

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

squares = list(map(lambda x: x * x, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
total = reduce(lambda x, y: x + y, numbers)

print("Squares:", squares)
print("Even numbers:", evens)
print("Sum:", total)