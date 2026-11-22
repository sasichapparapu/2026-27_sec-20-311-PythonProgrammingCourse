numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

numbers.append(int(input("Number to append: ")))
numbers.insert(int(input("Index to insert at: ")), int(input("Number to insert: ")))
numbers.remove(int(input("Number to remove: ")))

numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)