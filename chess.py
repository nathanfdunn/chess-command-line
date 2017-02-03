#!/usr/bin/env python3
# Copy this content to a file named 'chess', put it somewhere on your PATH and run `chmod +x chess`
# Put the 'chess-board.txt' file in the same folder as the 'chess' file

import pathlib
import sys
import os
here = pathlib.Path(__file__).parent

# Invert colors
os.system(r"printf '\e[7m'")

board = []
with open(here / 'chessboard.txt') as board_file:
    for line in board_file:
        board.append(list(line.strip('\n')))

def print_board(board):
    piece_map = dict(zip('kqrbnpKQRBNP', '♔♕♖♗♘♙♚♛♜♝♞♟'))

    pretty_board = [[None]*8 for i in range(8)]
    for i in range(8):
        for j in range(8):
            if board[i][j] not in piece_map:
                square = '::' if (i+j) % 2 else '  '
            else:
                square = piece_map[ board[i][j] ] + ' '
            pretty_board[i][j] = square

    char = '#'
    final = 20*char + '\n'
    for line in pretty_board:
        final += char + ' ' + ''.join(line) + ' ' + char + '\n'
    final += 20*char + '\n'
    print(final)

def write_board(board):
    with open(here / 'chessboard.txt', 'w') as board_file:
        for line in board:
            print(''.join(line), file=board_file)

# Converts to the y, x coords so you can do board[y][x]
# 'C3' -> 5, 2
def convert_coord(alg_notation):
    file, rank = alg_notation.upper()
    x = ord(file) - ord('A')
    y = 8 - int(rank)
    return y, x

# TODO make an ArgParser
if len(sys.argv) == 1:
    print_board(board)

elif len(sys.argv) == 3:
    start, end = sys.argv[1:]
    s_y, s_x = convert_coord(start)
    e_y, e_x = convert_coord(end)
    board[e_y][e_x] = board[s_y][s_x]
    board[s_y][s_x] = ' '
    write_board(board)
    print_board(board)

elif len(sys.argv) == 2:
    # Assume it's piece creation
    ...

else:
    print('Bad options')

# Revert colors
os.system(r"printf '\e[0m'")
