'''
Conrway's game on life
by Jérémy Saudemont
'''

from board import Board
import os

board = Board(155, 46)
board.draw_board()

while True:
    board.evolve()
    board.draw_board()
    # os.system('cls')
