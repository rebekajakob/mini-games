import random


# create board
def create_empty_board():
    board = []
    for row in range(4):
        board.append([str(0)] * 4)
    return board


def get_empty_indexes(board):
    empty_indexes = []
    for index in range(16):
        if board[index // 4][index % 4] == '0':
            empty_indexes.append(index)
    return empty_indexes


def get_place_for_random_number(empty_indexes):
    random_index = random.randint(0, len(empty_indexes))
    return random_index




