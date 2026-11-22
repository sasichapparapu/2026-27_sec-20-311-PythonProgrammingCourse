def simple_interest(principal, time, rate=5):
    return principal * time * rate / 100


principal = float(input("Enter principal: "))
time = float(input("Enter time in years: "))

print("Interest at default rate:", simple_interest(principal, time))

rate = float(input("Enter another rate: "))
print("Interest at entered rate:", simple_interest(principal, time, rate))