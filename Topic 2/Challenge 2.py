# Program to calculate the cost of word processing based on a fixed rate card
#----------------------------------------------------------------------------------------

import sys

# Declare constant variables
WORD_PER_MIN = 30
CHARGE_8_LESS = 21.75
CHARGE_8_PLUS = 25
HOUR_FACTOR = 60

# Ask user to provide number of words in a document
input_val = input('Please enter the number of words to type: ')

# Detect if number entered is a positive integer. Word count cannot be a float or negative numbers.
if not input_val.isnumeric():
    print('Please enter a whole positive integer number, try again.')
    sys.exit(1)

#Convert the string vaule from input into an integer
word_count = int(input_val)

#Convert words per 30 min to words per hour in int using Python Floor
work_hours = (word_count // WORD_PER_MIN)//HOUR_FACTOR
print(f'{word_count:,} words will take {work_hours:,}Hrs of labour.')

# Evaluate cost to customer for declared word count. Since rate card is per hour for word counts less than 1hr
# of labour a flat rate of $21.75 will be charged.
if work_hours >= 1 and work_hours <= 8:
    customer_cost = work_hours * CHARGE_8_LESS
    print(f'For a document containing {word_count:,} word will cost ${customer_cost:,.2f}')
elif work_hours == 0 and word_count <= 1800:
    print(f'For a document containing {word_count:,} word will cost a flat rate of ${CHARGE_8_LESS:,.2f}')
else:
    customer_cost = work_hours * CHARGE_8_PLUS
    print(f'For a document containing {word_count:,} word will cost ${customer_cost:,.2f}')

sys.exit(0)