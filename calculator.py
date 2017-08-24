"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here


def automated(file_name):

    math_operation = open(file_name)

    for line in math_operation:
        operator, num1, num2 = line.split()

    # tokens = input_string.split(' ')

        operator = tokens[0]

        operators = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']

        if operator not in operators:
            print 'Invalid input'
            continue

        if len(tokens) >= 2:

            num1 = int(tokens[1])

        if len(tokens) == 3:

            num2 = int(tokens[2])

        nums = tokens[1:]
        nums_list = []

        for num in nums:
            nums_list.append(int(num))

        if operator == '+':
            print '{:.2f}'.format(my_reduce(add, nums_list))

        elif operator == '-':
            print '{:.2f}'.format(my_reduce(subtract, nums_list))

        elif operator == '*':
            print '{:.2f}'.format(my_reduce(multiply, nums_list))

        elif operator == '/':
            print '{:.2f}'.format(my_reduce(divide, nums_list))

        elif operator == 'square':
            print '{:.2f}'.format(square(num1))

        elif operator == 'cube':
            print '{:.2f}'.format(cube(num1))

        elif operator == 'pow':
            print '{:.2f}'.format(my_reduce(power, nums_list))

        elif operator == 'mod':
            print '{:.2f}'.format(my_reduce(mod, nums_list))

        else:
            print 'Your input is invalid'



automated('operations.txt')

# loop until user enters 'q'
def my_reduce(function, lst):

    accum = lst[0]

    for item in lst[1:]:
        accum = function(accum, item)

    return accum


def user_input_calculator():
# while input_string != 'q' or input_string != 'quit'
    while True:
        input_string = raw_input('> ')

        if input_string == 'q' or input_string == 'quit':
            break

        tokens = input_string.split(' ')

        operator = tokens[0]

        operators = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']

        if operator not in operators:
            print 'Invalid input'
            continue

        if len(tokens) >= 2:

            num1 = int(tokens[1])

        if len(tokens) == 3:

            num2 = int(tokens[2])

        nums = tokens[1:]
        nums_list = []

        for num in nums:
            nums_list.append(int(num))

        if operator == '+':
            print '{:.2f}'.format(my_reduce(add, nums_list))

        elif operator == '-':
            print '{:.2f}'.format(my_reduce(subtract, nums_list))

        elif operator == '*':
            print '{:.2f}'.format(my_reduce(multiply, nums_list))

        elif operator == '/':
            print '{:.2f}'.format(my_reduce(divide, nums_list))

        elif operator == 'square':
            print '{:.2f}'.format(square(num1))

        elif operator == 'cube':
            print '{:.2f}'.format(cube(num1))

        elif operator == 'pow':
            print '{:.2f}'.format(my_reduce(power, nums_list))

        elif operator == 'mod':
            print '{:.2f}'.format(my_reduce(mod, nums_list))

        else:
            print 'Your input is invalid'






# iterate through list, calling the function on the accumulator
    # assign updated value to the accumlator with each iteration
# return final accumulated value



# tokenize input_string
    # if input_string[0] = any of the math functions
        # call that math function
        # arithmetic.multiply(num1, num2)
        # input_string[1] = num1
        # input_string[2] = num2







# operation_dictionary = {

#     '+': add
# }

# while True:
#     input_string = raw_input('> ')

#     tokens = input_string.split(' ')

#     final_value = operation_dictionary[tokens[0]](int(tokens[1]), int(tokens[2]))

#     print x

# operation_dictionary[tokens[0]]
# operation_dictionar['+']
