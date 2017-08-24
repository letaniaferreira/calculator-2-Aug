

#write a loop

def add(lst):
    """Return the sum of the two input integers."""

    sum = 0

    for num in lst:
        sum += num

    print sum


def subtract(lst):
    """Return the second number subtracted from the first."""
    sum = lst[0]

    lst2 = lst[1:]

    for num in lst2:
        sum -= num

    print sum


def multiply(lst):
    """Multiply the two inputs together."""

    product = 1

    for num in lst:
        product *= num

    print product


def divide(lst):
    """Divide the first input by the second, returning a floating point."""

    # Need to turn at least one argument to float for division to
    # not be integer division

    final_value = lst[0]

    lst2 = lst[1:]

    for num in lst2:
        final_value /= num

    print final_value


def square(lst):
    """Return the square of the input."""

    # Needs only one argument
    new_list = []

    for num in lst:
        new_list.append(num * num)

    print new_list


def cube(lst):
    """Return the cube of the input."""

    # Needs only one argument

    new_list = []

    for num in lst:
        new_list.append(num * num * num)

    print new_list


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
