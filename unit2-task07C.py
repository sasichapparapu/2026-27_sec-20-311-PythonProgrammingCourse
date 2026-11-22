rows = int(input("Enter the number of rows: "))
symbol = input("Enter the symbol to print (for example, * or 0): ")

for row in range(1, rows + 1):
    for column in range(row):
        print(symbol, end=" ")
    print()