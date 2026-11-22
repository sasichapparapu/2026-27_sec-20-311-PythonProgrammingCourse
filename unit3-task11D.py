balance = 1000

def deposit(amount):
    global balance
    balance += amount

def local_balance(amount):
    balance = amount
    print("Local balance:", balance)

deposit(500)
local_balance(200)

print("Account balance:", balance)