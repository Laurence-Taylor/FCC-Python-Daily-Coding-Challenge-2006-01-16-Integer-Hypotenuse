def is_integer_hypotenuse(a, b):
    # Calculate the hypotenuse value
    c = ((a**2 + b**2)**0.5)
    # If the calulated value of the hypostenuse divided by his own int value is exactly iqual 1,
    # then the value is an integer, otherwise is not
    # Return the True or False  
    return True if (c/int(c)) == 1 else False

if __name__ == '__main__':
    print(is_integer_hypotenuse(3, 4))
    print('---------')
    print(is_integer_hypotenuse(2, 3))
    print('---------')
    print(is_integer_hypotenuse(5, 12))
    print('---------')
    print(is_integer_hypotenuse(10, 10))
    print('---------')
    print(is_integer_hypotenuse(780, 1040))
    print('---------')
    print(is_integer_hypotenuse(250, 333))