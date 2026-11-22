def print_inverted_triangle(rows: int) -> None:
    if rows < 1:
        raise ValueError("rows must be a positive integer")

    for width in range(rows, 0, -1):
        print("* " * width)


rows = int(input("Enter the number of rows: "))
print_inverted_triangle(rows)