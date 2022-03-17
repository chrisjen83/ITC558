# Program to calculate the sum of positive integers

run_total = 0

print('Enter a series of positive numbers to calculate the sum, entering a negative number to end program.\n')
user_input = int(input('Please enter a positive number: '))

while not user_input <= -1:
    run_total += user_input
    user_input = int(input('Please enter a positive number: '))

print('\nTotal sum of numbers entered are:', run_total)