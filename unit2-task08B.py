number = int(input("Enter a whole number: "))
number = abs(number)  # Also handles negative numbers
total = 0

while number > 0:
    digit = number % 10
    total = total + digit
    number = number // 10

print("Sum of digits =", total)