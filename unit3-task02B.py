a = tuple(input("Enter first tuple items separated by spaces: ").split())
b = tuple(input("Enter second tuple items separated by spaces: ").split())

print("Concatenation:", a + b)
print("Slicing:", a[1:])

x, y, z = a
print("Unpacking:", x, y, z)