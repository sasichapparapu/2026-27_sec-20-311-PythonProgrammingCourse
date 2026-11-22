def print_pyramid(rows: int) -> None:
    if rows < 1:
        raise ValueError("rows must be a positive integer")

    for row in range(rows):
        spaces = " " * (rows - row - 1)
        stars = "*" * (2 * row + 1)
        print(spaces + stars)


rows = int(input("Enter the number of rows: "))
print_pyramid(rows)