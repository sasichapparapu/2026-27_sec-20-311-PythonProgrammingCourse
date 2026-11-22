def print_diamond(rows: int) -> None:
    if rows < 1:
        raise ValueError("rows must be a positive integer")

    for row in range(rows):
        print(" " * (rows - row - 1) + "*" * (2 * row + 1))

    for row in range(rows - 2, -1, -1):
        print(" " * (rows - row - 1) + "*" * (2 * row + 1))


rows = int(input("Enter the number of rows for the top half: "))
print_diamond(rows)