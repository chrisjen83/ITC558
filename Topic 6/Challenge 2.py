# Question 2 IsPrime

def is_prime(number):
    prime_flag = False

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                prime_flag = True

    if prime_flag:
        print(f'{number} is not a prime number')
    else:
        print(f'{number} is a prime number')


def main():
    user_input = int(input('Enter a number to determine if its a prime number: '))
    is_prime(user_input)


if __name__ == '__main__':
    main()