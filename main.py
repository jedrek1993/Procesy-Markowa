# -*- coding: utf-8 -*-
# matplotlib library is requirement, to get this >> sudo apt-get install python-matplotlib
import matplotlib.pyplot as plt

# For 4x4 world
N = 4
M = 4
S = {'x': 1, 'y': 1}
F = [{'x': 3, 'y': 1}, ]
T = [{'x': 4, 'y': 1, 'v': 100}, ]

# # For 4x3 world
# N = 4
# M = 3
# S = {'x': 1, 'y': 1}
# F = [{'x': 2, 'y': 2}, ]
# T = [{'x': 4, 'y': 3, 'v': 1}, {'x': 4, 'y': 2, 'v': -1}]


ACTIONS = ['^', '>', 'v', '<']
ACTION_P = [0.3, 0.3, 0.3, 0.1]


def main():
    policy = get_empty_board()
    utility = get_empty_board()
    policy = prepare_board(policy)
    utility = prepare_board(utility)
    ploted = [[0], [0], [0], [0], [0], [0], [None]]

    for i in range(20):
        for y in range(M):
            for x in range(N):
                if utility[y][x] is not 'F' and not is_terminal_state(x, y):
                    action_utility_sum = 4*[0]
                    # action ^
                    if y < M-1 and utility[y+1][x] is not 'F':
                        action_utility_sum[0] += ACTION_P[0]*utility[y+1][x]
                    else:
                        action_utility_sum[0] += ACTION_P[0]*utility[y][x]
                    if x > 0 and utility[y][x-1] is not 'F':
                        action_utility_sum[0] += ACTION_P[1]*utility[y][x-1]
                    else:
                        action_utility_sum[0] += ACTION_P[1]*utility[y][x]
                    if x < N-1 and utility[y][x+1] is not 'F':
                        action_utility_sum[0] += ACTION_P[2]*utility[y][x+1]
                    else:
                        action_utility_sum[0] += ACTION_P[2]*utility[y][x]
                    if y > 0 and utility[y-1][x] is not 'F':
                        action_utility_sum[0] += ACTION_P[3] * utility[y-1][x]
                    else:
                        action_utility_sum[0] += ACTION_P[3] * utility[y][x]

                    # action >
                    if x < N-1 and utility[y][x+1] is not 'F':
                        action_utility_sum[1] += ACTION_P[0]*utility[y][x+1]
                    else:
                        action_utility_sum[1] += ACTION_P[0]*utility[y][x]
                    if y < M-1 and utility[y+1][x] is not 'F':
                        action_utility_sum[1] += ACTION_P[1]*utility[y+1][x]
                    else:
                        action_utility_sum[1] += ACTION_P[1]*utility[y][x]
                    if y > 0 and utility[y-1][x] is not 'F':
                        action_utility_sum[1] += ACTION_P[2]*utility[y-1][x]
                    else:
                        action_utility_sum[1] += ACTION_P[2]*utility[y][x]
                    if x > 0 and utility[y][x-1] is not 'F':
                        action_utility_sum[1] += ACTION_P[3]*utility[y][x-1]
                    else:
                        action_utility_sum[1] += ACTION_P[3]*utility[y][x]

                    # action v
                    if y > 0 and utility[y-1][x] is not 'F':
                        action_utility_sum[2] += ACTION_P[0]*utility[y-1][x]
                    else:
                        action_utility_sum[2] += ACTION_P[0]*utility[y][x]
                    if x > 0 and utility[y][x-1] is not 'F':
                        action_utility_sum[2] += ACTION_P[2]*utility[y][x-1]
                    else:
                        action_utility_sum[2] += ACTION_P[2]*utility[y][x]
                    if x < N-1 and utility[y][x+1] is not 'F':
                        action_utility_sum[2] += ACTION_P[1]*utility[y][x+1]
                    else:
                        action_utility_sum[2] += ACTION_P[1]*utility[y][x]
                    if y < M-1 and utility[y+1][x] is not 'F':
                        action_utility_sum[2] += ACTION_P[3]*utility[y+1][x]
                    else:
                        action_utility_sum[2] += ACTION_P[3]*utility[y][x]

                    # action <
                    if x > 0 and utility[y][x-1] is not 'F':
                        action_utility_sum[3] += ACTION_P[0]*utility[y][x-1]
                    else:
                        action_utility_sum[3] += ACTION_P[0]*utility[y][x]
                    if y < M-1 and utility[y+1][x] is not 'F':
                        action_utility_sum[3] += ACTION_P[1]*utility[y+1][x]
                    else:
                        action_utility_sum[3] += ACTION_P[1]*utility[y][x]
                    if y > 0 and utility[y-1][x] is not 'F':
                        action_utility_sum[3] += ACTION_P[2]*utility[y-1][x]
                    else:
                        action_utility_sum[3] += ACTION_P[2]*utility[y][x]
                    if x < N-1 and utility[y][x+1] is not 'F':
                        action_utility_sum[3] += ACTION_P[3]*utility[y][x+1]
                    else:
                        action_utility_sum[3] += ACTION_P[3]*utility[y][x]

                    policy[y][x] = ACTIONS[action_utility_sum.index(max(action_utility_sum))]
                    utility[y][x] = -1 + 0.8*max(action_utility_sum)
                    if x == 2 and y == 1:
                        utility[y][x] -= 20

        ploted[0].append(utility[1][1])
        ploted[1].append(utility[1][3])
        ploted[2].append(utility[2][2])
        ploted[3].append(utility[2][1])
        ploted[4].append(utility[0][0])
        ploted[5].append(utility[1][0])
        ploted[6].append(utility[0][3])
    print "\n\tPolityka optymalna:"
    print_board(policy)
    print "\n\n\tUżyteczności stanów:"
    print_board(utility)
    print "\n"

    for pl in ploted:
        plt.plot(pl)
    plt.grid(True)
    plt.show()


def get_empty_board():
    board = []
    for x in range(M):
        board.append([0] * N)
    return board


def prepare_board(board):
    for a in F:
        board[a['y'] - 1][a['x'] - 1] = 'F'
    for a in T:
        board[a['y'] - 1][a['x'] - 1] = a['v']
    return board


def print_board(board):
    for row in board[::-1]:
        p = "\t"
        for elem in row:
            if type(elem) is float:
                p += "{0:6.4f} ".format(elem)
            elif type(elem) is int:
                p += "{:<+d}".format(elem)
            else:
                p += "{:6} ".format(elem)
        print p


def is_terminal_state(x, y):
    for state in T:
        if x == state['x']-1 and y == state['y']-1:
            return True
    return False


if __name__ == '__main__':
    main()
