n = int(input("How many numbers? "))

largest = int(input("Enter a number: "))

for i in range(n - 1):
    number = int(input("Enter a number: "))

    if number > largest:
        largest = number

print("The largest number is:", largest)