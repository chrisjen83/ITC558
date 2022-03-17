# Program to calculate track lap times

lap_min = []
lap_num = int(input('How many laps of the race track have you run? '))
print('\nEnter lap times in minuets\n')

# Allow user to enter lap times according to lap_num
for lap in range(lap_num):
    lap_time = int(input('Enter lap time: '))
    lap_min.append(lap_time)

# Sort the lap time list lowest ot highest
lap_min.sort()

# Fix index value
lap_num -= 1

# Calculate avg lap time
lap_avg = sum(lap_min) // lap_num

# Print slowest, fastest lap time and avg lap time.
print('\nLap results')
print(lap_min[0], 'min')
print(lap_min[lap_num], 'min')
print('Average lap time is', lap_avg, 'min')

