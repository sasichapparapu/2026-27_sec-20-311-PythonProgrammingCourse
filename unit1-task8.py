n = int(input("Enter a positive integer N: "))

if n < 1:
    print("N must be a positive integer.")
else:
    total = n * (n + 1) // 2
    print(f"Sum of the first {n} natural numbers: {total}")