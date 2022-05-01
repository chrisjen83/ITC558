# Question 1

import random


def generate_rand(u_input):
    even_count = 0
    odd_count = 0

    for number in range(u_input):
        num = random.randint(1, 100)

        if (num % 2) == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count


def main():
    user_input = int(input('How many random numbers do you require? '))

    pos_count, neg_count = generate_rand(user_input)

    print(f'Even Numbers: {pos_count}')
    print(f'Odd Numbers: {neg_count}')


if __name__ == '__main__':
    main()