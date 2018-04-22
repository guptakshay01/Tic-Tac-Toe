from __future__ import print_function
import random
import os

#--Display Game board--#
def display_board(board):
    os.system('cls')
    print('\n')
    print(' ' + board[7] + ' | ' + board[8] +' | '+ board[9])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] +' | '+ board[6])
    print('---|---|---')
    print(' ' + board[1] + ' | ' + board[2] +' | '+ board[3])

#--Check the Player Input--#
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input('Player 1: Do you want take X or O: ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'

#--Position of Mark--#
def place_marker(board, marker, position):
        board[position] = marker

#--Check who Won--#
def win_check(board, mark):
    return((board[7] == mark and board[8] == mark and board[9] == mark) or
           (board[4] == mark and board[5] == mark and board[6] == mark) or
           (board[3] == mark and board[2] == mark and board[1] == mark) or
           (board[7] == mark and board[4] == mark and board[1] == mark) or
           (board[8] == mark and board[5] == mark and board[2] == mark) or
           (board[9] == mark and board[6] == mark and board[3] == mark) or
           (board[7] == mark and board[5] == mark and board[3] == mark) or
           (board[9] == mark and board[5] == mark and board[1] == mark))

#--To choose which Player goes first--#
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

#--Check position is empty or not--#
def space_check(board, position):
    return board[position] == ' '

#--Check if board is full or not--#
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


#--Next position for move--#
def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = raw_input('Choose your next position: (1-9)')
    return int(position)


def replay():
    return raw_input('Do you want to play again? y or n: ').lower().startswith('y')





print('Welcome to Tic Tac Toe!')
while(True):
    gameBoard = [' '] * 10
    player1_mark, player2_mark = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':

            #Player 1 turn
            display_board(gameBoard)
            position = player_choice(gameBoard)
            place_marker(gameBoard, player1_mark, position)

            if win_check(gameBoard, player1_mark):
                display_board(gameBoard)
                print('Player 1 won the game!')
                game_on = False
            else:
                if full_board_check(gameBoard):
                    display_board(gameBoard)
                    print('The game is draw!')
                    break
                else:
                    turn = 'Player 2'
        else:

            #Player 2 turn
            display_board(gameBoard)
            position = player_choice(gameBoard)
            place_marker(gameBoard, player2_mark, position)

            if win_check(gameBoard, player2_mark):
                display_board(gameBoard)
                print('Player 2 won the game!')
                game_on = False
            else:
                if full_board_check(gameBoard):
                    display_board(gameBoard)
                    print('The game is tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break