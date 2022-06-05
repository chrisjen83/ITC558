import converter


def main():
    inches = float(input('Enter a measurement in inches to convert: '))

    calc_feet = converter.feet_to_inches(inches)

    print(f'{inches:.3f} inches is {calc_feet:.3f} feet')

main()