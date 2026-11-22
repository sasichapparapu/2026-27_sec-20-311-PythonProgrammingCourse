number = int(input("Enter a number: "))
number = abs(number)  # Makes a negative number positive
count = 0

if number == 0:
    count = 1
else:
    while number > 0:
        count = count + 1
        number = number // 10

print("Number of digits =", count)