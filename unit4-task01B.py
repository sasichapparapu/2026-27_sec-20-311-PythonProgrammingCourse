try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Error: cannot divide by zero.")