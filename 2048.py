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
        add_random_number(empty_board, first_placement_chances[i])
    return empty_board


def add_random_number(board, first_placement_chances):
    empty_indexes = get_empty_indexes(board)
    random_place = get_place_for_random_number(empty_indexes)
    random_number = get_random_number(first_placement_chances)
    board[random_place // 4][random_place % 4] = random_number


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


def get_valid_direction():
    get_direction_input = input("Choose a direction (w a s d): ").lower()
    while get_direction_input not in ['w', 'a', 's', 'd']:
        get_direction_input = input("Choose a valid direction (w a s d): ")
    return get_direction_input


def search_rest_of_row(row, col, from_index, to_index, direction):
    for index in range(from_index, to_index):
        if row[(len(row) + index * direction - 1) // len(row)] != '0':
            row[col] = row[index]
            row[index] = '0'
            return row
    return row


def place_horizontal(board, direction):
    for row in board:
        for col in range(0, len(row)):
            if row[(len(row) + col * direction - 1) // len(row)] == '0':
                if direction == 1:
                    row = search_rest_of_row(row, col, col, len(row), direction)
                else:
                    row = search_rest_of_row(row, col, 0, col, direction)
                if row[col] == '0':
                    break


def move_to_horizontal_edge(board, direction, from_index, to_index):
    for row in board:
        for col in range(from_index, len(row)):
            if row[col * direction] == '0':
                for index in range(col + 1, to_index):
                    if row[index * direction] != '0':
                        row[col * direction] = row[index * direction]
                        row[index * direction] = '0'
                        break


def move(direction_input, board):
    if direction_input == 'a':
        move_to_horizontal_edge(board, 1, 0, 4)
        for row in board:
            for col in range(1, len(row)):
                if row[col] != '0':
                    if row[col] == row[col - 1]:
                        row[col - 1] = str(int(row[col - 1]) * 2)
                        row[col] = '0'
        move_to_horizontal_edge(board, 1, 0, 4)

    if direction_input == 'd':
        move_to_horizontal_edge(board, -1, 1, 5)
        for row in board:
            for col in range(1, len(row)):
                if row[-col] != '0':
                    if row[-col] == row[-col - 1]:
                        row[-col] = str(int(row[-col]) * 2)
                        row[-col - 1] = '0'
        move_to_horizontal_edge(board,-1, 1, 5)

    if direction_input == 'w':
        for col in range(0, len(board)):
            for row in range(0, len(board)):
                if board[row][col] == '0':
                    for index in range(row, len(board)):
                        if board[index][col] != '0':
                            board[row][col] = board[index][col]
                            board[index][col] = '0'
                            break

        for col in range(0, len(board)):
            for row in range(0, len(board)):
                if board[row][col] != '0':
                    if board[row][col] == board[row + 1][col]:
                        board[row][col] = str(int(board[row][col])*2)
                        board[row + 1][col] = '0'

    if direction_input == 's':
        for col in range(0, len(board)):
            for row in range(1, len(board)+1):
                if board[-row][col] == '0':
                    for index in range(row, len(board) + 1):
                        if board[-index][col] != '0':
                            board[-row][col] = board[-index][col]
                            board[-index][col] = '0'
                            break
        for col in range(0, len(board)):
            for row in range(1, len(board)+1):
                if board[-row][col] != '0':
                    if board[-row][col] == board[-row - 1][col]:
                        board[-row][col] = str(int(board[-row][col])*2)
                        board[-row - 1][col] = '0'


def game_2048():
    game_on = True
    board = create_starter_board()
    print_board(board)
    while game_on is True:
        direction_input = get_valid_direction()
        move(direction_input, board)
        print_board(board)



if __name__ == '__main__':
    game_2048()

