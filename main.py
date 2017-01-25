# -*- coding: utf-8 -*-
from random import random


N = 4
M = 3
S = {'x': 1, 'y': 1}
F = [{'x': 2, 'y': 2}, ]
T = [{'x': 4, 'y': 3, 'v': 1}, {'x': 4, 'y': 2, 'v': -1}, ]
B = []
ACTIONS = ['^', '>', 'v', '<']
ACTION_P = [0.8, 0.1, 0.1, 0]


def main():
    policy = get_empty_board()
    utility = get_empty_board()
    policy = prepare_board(policy)
    utility = prepare_board(utility)

    for _ in range(2):
        for y in range(M):
            for x in range(N):
                action_utility_sum = 4*[0]
                for action in range(4):
                    action_utility_sum[action] = random()  # Tu powinno być obliczanie U*P
                policy[y][x] = ACTIONS[action_utility_sum.index(max(action_utility_sum))]





    print_board(policy)
    print ""
    print_board(utility)



def get_empty_board():
    board = []
    for x in range(M):
        board.append([0] * N)
    return board


def prepare_board(board):
    board[S['y'] - 1][S['x'] - 1] = 'S'
    for a in F:
        board[a['y'] - 1][a['x'] - 1] = 'F'
    for a in T:
        board[a['y'] - 1][a['x'] - 1] = a['v']
    for a in B:
        board[a['y'] - 1][a['x'] - 1] = a['v']
    return board


def print_board(board):
    for row in board[::-1]:
        print row


if __name__ == '__main__':
    main()
