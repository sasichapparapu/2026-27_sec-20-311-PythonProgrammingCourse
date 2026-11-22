n = int(input("How many numbers? "))
total = 0

for i in range(n):
    number = int(input("Enter a number: "))
    total = total + number

average = total / n

print("Sum =", total)
print("Average =", average)