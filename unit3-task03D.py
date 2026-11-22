def calculate(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average


m1 = float(input("Enter first subject marks: "))
m2 = float(input("Enter second subject marks: "))
m3 = float(input("Enter third subject marks: "))

total, average = calculate(m1, m2, m3)

print("Total:", total)
print("Average:", average)