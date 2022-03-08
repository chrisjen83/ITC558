# Program to display point for a customers purchase.
#----------------------------------------------------------------------------------------

import sys

#Ask customer to enter total sale value
input_val = input('Please enter you the total sales cost in dollars $')

# Detect if number entered is integer which is either positive or negative.
# If a float or text is entered program will exit.
try:
    int(input_val)
except ValueError:
    print('You did not enter the amount in dollars, try again...')
    sys.exit(1)

sale_total = int(input_val)

#Evaluate the customers spend to the points table
if sale_total >= 0 and sale_total <= 100:
    print('You have received 10 Points. Congratulations')
elif sale_total >= 101 and sale_total <= 500:
    print('You have received 20 Points. Congratulations')
elif sale_total >= 501:
    print('You have received 50 Points. Congratulations')
else:
    print('Your spend does not qualify for any points. Sorry')

sys.exit(0)