principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time in years: "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print(f"Final amount: {amount:.2f}")
print(f"Compound interest: {compound_interest:.2f}")