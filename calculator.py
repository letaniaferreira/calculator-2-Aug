"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here


# loop until user enters 'q'

# while input_string != 'q' or input_string != 'quit'
while True:
    input_string = raw_input('> ')

    if input_string == 'q' or input_string == 'quit':
        break

    tokens = input_string.split(' ')

    operator = tokens[0]

    if len(tokens) >= 2:

        num1 = int(tokens[1])

    if len(tokens) == 3:

        num2 = int(tokens[2])

    if operator == '+':
        print add(num1, num2)

    elif operator == '-':
        print subtract(num1, num2)

    elif operator == '*':
        print multiply(num1, num2)

    elif operator == '/':
        print divide(num1, num2)

    elif operator == 'square':
        print square(num1)

    elif operator == 'cube':
        print cube(num1)

    elif operator == 'pow':
        print power(num1, num2)

    elif operator == 'mod':
        print mod(num1, num2)

    else:
        print 'Your input is invalid'






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
