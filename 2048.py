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
    random_index = random.randint(0, len(empty_indexes)-1)
    return empty_indexes[random_index]


def get_random_number(probability_of_two):
    random_number = random.randint(0, 100)
    if random_number < probability_of_two:
        return '2'
    return '4'


def create_starter_board():
    empty_board = create_empty_board()
    first_placement_chances = [100, 70]
    for i in range(2):
        empty_indexes = get_empty_indexes(empty_board)
        random_place = get_place_for_random_number(empty_indexes)
        random_number = get_random_number(first_placement_chances[i])
        empty_board[random_place // 4][random_place % 4] = random_number
    return empty_board


def print_board(board):
    printed = ""
    longest_number_size = max([len(max(lst, key=len)) for lst in board])
    for row in range(len(board)):
        printed += "-" * 5 * (longest_number_size+4) + "\n"
        print_row = "|"
        for col in range(len(board[row])):
            empty_space_len = 2 + ((longest_number_size - len(board[row][col])) // 2)
            print_row += " " * empty_space_len + board[row][col] + " " * empty_space_len + "|"
        print_row += "\n"
        printed += print_row
    printed += "-" * 5 * (longest_number_size+4) + "\n"
    print(printed)

