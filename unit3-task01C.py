a = set(map(int, input("Enter numbers for set A: ").split()))
b = set(map(int, input("Enter numbers for set B: ").split()))

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)