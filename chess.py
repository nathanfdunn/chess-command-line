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

def square_string(piece, square_is_white):
    out = ''
    if piece.lower() in 'kqrbnp':
        piece_is_white = piece in 'KQRBNP'.lower()      #yeah, yeah. We'll be FEN compliant soon
        if piece_is_white == square_is_white:
            # We need the outline version
            piece_char = dict(zip('kqrbnp', '♔♕♖♗♘♙'))[piece.lower()] + ' '
        else:
            # We can use the solid version
            piece_char = dict(zip('kqrbnp', '♚♛♜♝♞♟'))[piece.lower()] + ' '
    else:
        piece_char = '  '

    if square_is_white:
        out += r'\e[0;30;47m'
    else:
        out += r'\e[0;37;40m'

    out += piece_char
    return out

def print_board(board, border=False):
    string = r"printf '\e[0m"
    if border:
        string += r'<>================<>\n'
    for i, row in enumerate(board):
        string += r'\e[0m' + ('||' if border else '')
        for j, piece in enumerate(row):
            string += square_string(board[i][j], (i+j) % 2)
        string += r'\e[0m' + ('||' if border else '') + r'\n'
    if border:
        string += '<>================<>\n'
    string += "'"
    with open('print-chessboard.sh', 'w') as f:
        f.write(string)
    os.system(string)

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
