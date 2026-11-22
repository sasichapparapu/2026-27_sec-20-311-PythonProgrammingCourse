items = set(input("Enter items separated by spaces: ").split())

item = input("Enter an item to check: ")
print("Is in set:", item in items)

items.add(input("Enter item to add: "))
items.remove(input("Enter item to remove: "))
items.discard(input("Enter item to discard: "))

print("Updated set:", items)
