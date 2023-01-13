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
        printed += "-" * 5 * 5 + "\n"
        print_row = "|"
        for col in range(len(board[row])):
            empty_space_len = (6 - len(board[row][col])) // 2
            get_colored_text = color_numbers(board[row][col])
            if len(board[row][col]) % 2 != 0:
                print_row += " " * empty_space_len + get_colored_text + " " * empty_space_len + "|"
            else:
                print_row += " " * (empty_space_len - 1) + get_colored_text + " " * empty_space_len + "|"
        print_row += "\n"
        printed += print_row
    printed += "-" * 5 * 5 + "\n"
    print(printed)


def color_numbers(cell):
    end = '\033[0m'
    if cell == '0':
        return ' '
    elif cell == '2':
        return '\033[94m' + '2' + end
    elif cell == '4':
        return '\033[38;5;205m' + '4' + end
    elif cell == '8':
        return '\033[38;2;243;134;48m' + '8' + end
    elif cell == '16':
        return '\033[1;36m' + '16' + end
    elif cell == '32':
        return '\033[1;32m' + '32' + end
    elif cell == '64':
        return '\033[1;33m' + '64' + end
    elif cell == '128':
        return '\033[1;35m' + '128' + end
    elif cell == '256':
        return '\033[92m' + '256' + end
    elif cell == '514':
        return '\033[96m' + '514' + end
    elif cell == '1024':
        return '\033[1;31m' + '1024' + end
    else:
        return cell



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
                    if row != len(board)-1:
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
            for row in range(1, len(board)):
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
        add_random_number(board, 70)
        print_board(board)


if __name__ == '__main__':
    game_2048()

