# Program to displays the middle of three inputs
#----------------------------------------------------------------------------------------

# Ask the user to enter three numbers.
a, b, c = input('Enter three number from 1-9 separated by a space: ').split()

#Find the middle number
middle_num = sorted([a, b, c])[1]
print('The middle number is ', middle_num)