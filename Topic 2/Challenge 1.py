# Program to test integer attributes. This program will test positive/negative and zero
# as well as odd and even number.
#----------------------------------------------------------------------------------------

import sys

# user enter number to test
input_val = input('Enter a whole number to test: ')

# Detect if number entered is integer which is either positive or negative.
# If a float or text is entered program will exit.
try:
    int(input_val)
except ValueError:
    print('Please enter a whole integer number, try again.')
    sys.exit(1)

#Convert the string vaule from input into an integer
num = int(input_val)

# Test for positive/negative or zero number
if num > 0:
    print(num, 'is a POSITIVE number')
elif num == 0:
    print(num, 'is Zero')
else:
    print(num, ' is a NEGATIVE number')

# Test to determine if number is odd or even
if num % 2 == 0:
    print(num, 'is an even number.')
else:
    print(num, 'is an odd number.')

sys.exit(0)