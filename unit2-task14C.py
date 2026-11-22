rows = int(input("Enter number of rows: "))
number = 1

for i in range(1, rows + 1):
    for _ in range(i):
        print(number, end=" ")
        number += 1
    print()