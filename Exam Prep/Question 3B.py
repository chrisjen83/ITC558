

again = 'y'

while again == 'y':
    num_1 = float(input('Enter first numbers: '))
    num_2 = float(input('Enter second numbers: '))
    result = num_1 + num_2
    print(f'The sum of {num_1} and {num_2} is {result:,.2f}')

    again = input('Would you like to continue? ')
