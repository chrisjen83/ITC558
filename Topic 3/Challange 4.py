
semester_fee = 8000
FEE_INCREASE = 0.02

# Convert semester into yearly fee
year_fee = semester_fee * 2

for year in range(5):
    year_fee += year_fee * FEE_INCREASE
    print('Year', (year+1), 'Tuition Fee will be $', format(year_fee, ',.2f'))
