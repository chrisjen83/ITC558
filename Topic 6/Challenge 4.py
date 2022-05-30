# Scissors, Paper Rock Game

import random

def computer_move():
    move = random.randrange(1,3,1)

    return move

def human_move():
    print('Welcome to Scissors, Paper, Rock Game. Enter below your move.')
    print('Scissors = 3, Paper = 2 and Rock = 1')

    move = int(input('Enter your move (1,2 or 3): '))

    return move

def winner(comp_move, hum_move):
    comp_win = 0
    hum_win = 0

    if comp_move > hum_move and not 1:
        comp_win += 1
    elif comp_move < hum_move:
        hum_win += 1
    elif comp_move == 3 and hum_move == 1:
        hum_win += 1
    else:
        comp_win += 1

    return comp_win, hum_win



h_move = human_move()
c_move =  computer_move()
c_winner, h_winner = winner(c_move, h_move)

print(f'Computer: {c_winner}, Human: {h_winner}')

