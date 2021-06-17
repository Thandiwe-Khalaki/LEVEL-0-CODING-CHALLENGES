def maximum_number(*args):
    """Takes a list of *args and returns the biggest number"""
    biggest_number = args[0]
    for i in args:
        if i > biggest_number:
            biggest_number = i
    return biggest_number


print(maximum_number(102.03, 11115555,108**2,1000000))