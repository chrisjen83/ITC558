
tot_years = int(input('Enter the number of year: '))
tot_rain = 0
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May','Jun', 'Jul', 'Aug','Sep','Oct', 'Nov','Dec']
MONTH_IN_YR = 12

for year in range(tot_years):
    for month in MONTHS:
        rain = int(input('Enter the amount of rain in mm for {} : '.format(month)))
        tot_rain += rain
        tot_months = tot_years * MONTH_IN_YR
        avg_rain = tot_rain / tot_months

print('\nTotal number of months recorded is {}'.format(tot_months))
print('Total rainfall recorded is {}mm'.format(tot_rain))
print('Average rainfall for {} months is {}mm'.format(tot_months,avg_rain))

