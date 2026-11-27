try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input: please enter a whole number.")
else:
    print(number ** 2)
finally:
    print("Program finished")