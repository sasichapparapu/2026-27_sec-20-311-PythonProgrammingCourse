def find_sum(*args):
    return sum(args)


numbers = map(float, input("Enter numbers separated by spaces: ").split())
print("Sum:", find_sum(*numbers))