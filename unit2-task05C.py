size = int(input("Enter the grid size: "))

for row in range(size):
    for column in range(size):
        print("*", end=" ")
    print()