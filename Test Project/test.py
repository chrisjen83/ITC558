import boto3

hours = int(input('How many hours worked? '))
hour_type = type(hours)
print(hour_type)
pay_rate = float(input('What is your pay rate? '))

gross_pay = format((hours * pay_rate), '.2f')

print('The total pay is $', gross_pay)
