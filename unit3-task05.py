a = []
b = []

print("Enter 4 numbers for matrix A:")
for i in range(2):
    a.append(list(map(int, input().split())))

print("Enter 4 numbers for matrix B:")
for i in range(2):
    b.append(list(map(int, input().split())))

print("Addition:")
for i in range(2):
    print(a[i][0] + b[i][0], a[i][1] + b[i][1])

print("Subtraction:")
for i in range(2):
    print(a[i][0] - b[i][0], a[i][1] - b[i][1])