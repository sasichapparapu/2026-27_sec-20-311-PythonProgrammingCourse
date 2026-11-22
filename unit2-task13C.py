n = int(input("Enter number of rows: "))

row = [1]

for _ in range(n):
    print(" ".join(map(str, row)).center(2 * n))

    next_row = [1]
    for i in range(len(row) - 1):
        next_row.append(row[i] + row[i + 1])
    next_row.append(1)

    row = next_row