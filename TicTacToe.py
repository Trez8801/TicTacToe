import random

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
clear = [0]


def display_board(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + str(board[0][0]) + '   |   ' + str(board[0][1]) + '   |   ' + str(board[0][2]) + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + str(board[1][0]) + '   |   ' + str(board[1][1]) + '   |   ' + str(board[1][2]) + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + str(board[2][0]) + '   |   ' + str(board[2][1]) + '   |   ' + str(board[2][2]) + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')


def cpu_move(board):
    while True:
        turns = [5]
        for i in range(8):
            computerMove = random.choice([i for i in range(1, 10) if i not in turns])  # give this line for assignment
            turns.append(computerMove)
            if turns[-1] in board[0]:
                if turns[-1] == 1:
                    board[0][0] = 'X'
                    break
                elif turns[-1] == 2:
                    board[0][1] = 'X'
                    break
                elif turns[-1] == 3:
                    board[0][2] = 'X'
                    break
            elif turns[-1] in board[1]:
                if turns[-1] == 4:
                    board[1][0] = 'X'
                    break
                elif turns[-1] == 6:
                    board[1][2] = 'X'
                    break
            elif turns[-1] in board[2]:
                if turns[-1] == 7:
                    board[2][0] = 'X'
                    break
                elif turns[-1] == 8:
                    board[2][1] = 'X'
                    break
                elif turns[-1] == 9:
                    board[2][2] = 'X'
                    break
        break


def player_move(board):
    while True:
        global user_input
        user_input = int(input('Enter your move or enter 0 to clear the board: '))
        if user_input in clear:
            return
        if user_input < 0 or user_input > 9:
            print('A number between 1-9.')
            continue
        elif user_input not in board[0] and user_input not in board[1] and user_input not in board[2]:
            print('that space is occupied.')
            continue
        for i in range(len(board)):
            i = user_input
            if i in board[0]:
                if i == 1:
                    board[0][0] = 'O'
                    break
                elif i == 2:
                    board[0][1] = 'O'
                    break
                elif i == 3:
                    board[0][2] = 'O'
                    break
            elif i in board[1]:
                if i == 4:
                    board[1][0] = 'O'
                    break
                elif i == 6:
                    board[1][2] = 'O'
                    break
            elif i in board[2]:
                if i == 7:
                    board[2][0] = 'O'
                    break
                elif i == 8:
                    board[2][1] = 'O'
                    break
                elif i == 9:
                    board[2][2] = 'O'
                    break
        break


def winner(board):
    user_won = 'Congratulations, you won.'
    cpu_won = 'You lost...lol.'
    X = 'X', 'X', 'X'
    O = 'O', 'O', 'O'
    diagonal_right = board[0][0], board[1][1], board[2][2]
    diagonal_left = board[0][2], board[1][1], board[2][0]
    down_left = board[0][0], board[1][0], board[2][0]
    down_mid = board[0][1], board[1][1], board[2][1]
    down_right = board[0][2], board[1][2], board[2][2]
    across_top = board[0][0], board[0][1], board[0][2]
    across_mid = board[1][0], board[1][1], board[1][2]
    across_bottom = board[2][0], board[2][1], board[2][2]

    if X == diagonal_right or X == diagonal_left:
        return print(cpu_won)
    elif X == down_left or X == down_mid or X == down_right:
        return print(cpu_won)
    elif X == across_top or X == across_mid or X == across_bottom:
        return print(cpu_won)
    elif O == down_left or O == down_right:
        return print(user_won)
    elif O == across_top or O == across_bottom:
        return print(user_won)
    else:
        return False


def reset(board):
    if user_input in clear:
        board[0][0] = 1
        board[0][1] = 2
        board[0][2] = 3
        board[1][0] = 4
        board[1][1] = 'X'
        board[1][2] = 6
        board[2][0] = 7
        board[2][1] = 8
        board[2][2] = 9
        return
    else:
        return False


def tied(board):
    if board[0][0] != 1:
        if board[0][1] != 2:
            if board[0][2] != 3:
                if board[1][0] != 4:
                    if board[1][2] != 6:
                        if board[2][0] != 7:
                            if board[2][1] != 8:
                                if board[2][2] != 9:
                                    return True
    else:
        return False



def game(board):
    while True:
        display_board(board)
        if player_move(board) == winner(board):
            display_board(board)
            return
        elif cpu_move(board) == winner(board):
            display_board(board)
            return
        elif reset(board):
            display_board(board)
            return
        if tied(board):
            display_board(board)
            return print('Tied Game.')


game(board)
another = input('Do you want to play again? ')
if another == 'yes':
    while another == 'yes':
        board[0][0] = 1
        board[0][1] = 2
        board[0][2] = 3
        board[1][0] = 4
        board[1][1] = 'X'
        board[1][2] = 6
        board[2][0] = 7
        board[2][1] = 8
        board[2][2] = 9
        game(board)
        another = input('Do you want to play again? ')
elif another == 'no':
    print('Good Game.')

if another != 'yes':
    if another != 'no':
        while another != 'yes' or 'no':
            print('I don\'t understand?')
            another = input('Enter yes or no. ')
            if another == 'yes':
                board[0][0] = 1
                board[0][1] = 2
                board[0][2] = 3
                board[1][0] = 4
                board[1][1] = 'X'
                board[1][2] = 6
                board[2][0] = 7
                board[2][1] = 8
                board[2][2] = 9
                game(board)
                another = input('Do you want to play again? ')
            if another == 'no':
                print('Good Game.')
                break