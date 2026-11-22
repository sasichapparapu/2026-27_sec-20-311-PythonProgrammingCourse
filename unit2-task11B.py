number = int(input("Enter a 3-digit number: "))
original = number
total = 0

while number > 0:
    digit = number % 10
    total = total + digit * digit * digit
    number = number // 10

if total == original:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")