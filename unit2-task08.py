number = int(input("Enter a number between 1 and 100: "))

if number < 2:
    print("It is not a prime number.")
else:
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print("It is a prime number.")
    else:
        print("It is not a prime number.")