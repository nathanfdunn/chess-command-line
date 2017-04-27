#!/usr/bin/env python3
# Copy this content to a file named 'chess', put it somewhere on your PATH and run `chmod +x chess`
# Put the '.chessboard' file in the same folder as the 'chess' file

import pathlib
import sys
import os
here = pathlib.Path(__file__).parent

def get_board():
    board = []
    with open(here / '.chessboard') as board_file:
        for i in range(8):
            line = next(board_file, '')
            line = line.strip('\n').ljust(8)
            board.append(list(line))
        print(board_file.read())
    return board

def print_board(board):
    # Invert colors
    os.system(r"printf '\e[7m'")
    piece_map = dict(zip('kqrbnpKQRBNP', '♔♕♖♗♘♙♚♛♜♝♞♟'))

    pretty_board = [[None]*8 for i in range(8)]
    for i in range(8):
        for j in range(8):
            if board[i][j] in piece_map:
                square = piece_map[ board[i][j] ] + ' '
            else:
                square = '::' if (i+j) % 2 else '  '
            pretty_board[i][j] = square

    border = '#'
    final = 20*border + '\n'
    for line in pretty_board:
        final += border + ' ' + ''.join(line) + ' ' + border + '\n'
    final += 20*border + '\n'
    print(final)
    # Revert colors
    os.system(r"printf '\e[0m'")

def write_board(board):
    with open(here / '.chessboard', 'w') as board_file:
        for line in board:
            print(''.join(line), file=board_file)

def reset_board():
    with open(here / '.chessboard', 'w') as board_file:
        board_file.write('RNBQKBNR\nPPPPPPPP\n\n\n\n\npppppppp\nrnbqkbnr')

# Converts to the y, x coords so you can do board[y][x]
# 'C3' -> 5, 2
def convert_coord(alg_notation):
    file, rank = alg_notation.upper()
    x = ord(file) - ord('A')
    y = 8 - int(rank)
    return y, x








# TODO make an ArgParser
if len(sys.argv) == 1:
    print_board(get_board())

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'reset':
        reset_board()
    else:
        print('Bad options')

elif len(sys.argv) == 3:
    board = get_board()
    start, end = sys.argv[1:]
    s_y, s_x = convert_coord(start)
    e_y, e_x = convert_coord(end)
    board[e_y][e_x] = board[s_y][s_x]
    board[s_y][s_x] = ' '
    write_board(board)
    print_board(board)

else:
    print('Bad options')


