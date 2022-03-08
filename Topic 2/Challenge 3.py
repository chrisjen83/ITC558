# Program to calculate the cost of word processing based on a fixed rate card
#----------------------------------------------------------------------------------------

import sys

#Seating price tiers
CLASS_A = 50
CLASS_B = 30
CLASS_C = 15
SEAT_CAT_LIST = ['A', 'B', 'C']

#Ask you for seating catagory letter
input_val = input('Please enter a seat category. Enter A,B or C: ')

# Normalise seat category letter so user can enter UPPER or lower case.
seat_cat = input_val.upper()

# Test the user has entered the correct choices.
if not seat_cat in SEAT_CAT_LIST:
    print('You entered', seat_cat, 'this is incorrect.')
    print('Please enter the correct seat category, either A, B or C. Try again...')
    sys.exit(1)

# Evaluate correctly entered seating class and display cost.
if seat_cat == 'A':
    print(f'The cost of Class {seat_cat} seating is ${CLASS_A:,.2f}')
elif seat_cat == 'B':
    print(f'The cost of Class {seat_cat} seating is ${CLASS_B:,.2f}')
else:
    print(f'The cost of Class {seat_cat} seating is ${CLASS_C:,.2f}')

sys.exit(0)