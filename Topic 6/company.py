import customer

user_input = int(input('Enter the total customer purchases: '))

total_points = customer.calculate_points(user_input)

print(f'The total points for customer purchase is {total_points}')