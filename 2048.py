import random


# create board
def create_empty_board():
    board = []
    for row in range(4):
        board.append([str(0)] * 4)

