items = ["apple", "banana", "cherry"]

try:
    index = int(input("Enter a list index: "))
    print(items[index])
except ValueError:
    print("Invalid input: please enter an integer.")
except IndexError:
    print(f"Index out of range. Enter a value from {-len(items)} to {len(items) - 1}.")