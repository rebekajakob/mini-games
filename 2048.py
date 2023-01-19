import random
import os


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
    if len(empty_indexes) != 0:
        random_place = get_place_for_random_number(empty_indexes)
        random_number = get_random_number(first_placement_chances)
        board[random_place // 4][random_place % 4] = random_number


def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    printed = ""
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
    elif cell == '512':
        return '\033[96m' + '512' + end
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


def move_to_vertical_edge(board, direction, from_index, to_index):
    for col in range(0, len(board)):
        for row in range(from_index, to_index):
            if board[row * direction][col] == '0':
                for index in range(row, to_index):
                    if board[index * direction][col] != '0':
                        board[row * direction][col] = board[index * direction][col]
                        board[index * direction][col] = '0'
                        break


def sum_numbers_vertical(board, direction, from_index, to_index):
    for col in range(0, len(board)):
        for row in range(from_index, len(board)):
            if board[row * direction][col] != '0':
                if row != to_index:
                    if board[row * direction][col] == board[(row + 1) * direction][col]:
                        board[row * direction][col] = str(int(board[row * direction][col]) * 2)
                        board[(row + 1) * direction][col] = '0'


def sum_numbers_horizontal(board, direction, from_index, to_index):
    for row in board:
        for col in range(from_index, to_index):
            if row[col * direction] != '0':
                if row != to_index:
                    if row[col * direction] == row[(col - 1) * direction]:
                        row[(col - 1) * direction] = str(int(row[(col - 1) * direction]) * 2)
                        row[col * direction] = '0'


def can_be_sum_vertical(board, direction, from_index, to_index):
    for col in range(0, len(board)):
        for row in range(from_index, len(board)):
            if board[row * direction][col] != '0':
                if row != to_index:
                    if board[row * direction][col] == board[(row + 1) * direction][col]:
                        return True


def can_be_sum_horizontal(board, direction, to_index):
    for row in board:
        for col in range(1, to_index):
            if row[col * direction] != '0':
                if row[col * direction] == row[(col - 1) * direction]:
                    return True


def move(direction_input, board):
    if direction_input == 'a':
        move_to_horizontal_edge(board, 1, 0, 4)
        sum_numbers_horizontal(board, 1, 1, 4)
        move_to_horizontal_edge(board, 1, 0, 4)
    if direction_input == 'd':
        move_to_horizontal_edge(board, -1, 1, 5)
        sum_numbers_horizontal(board, -1, 2, 5)
        move_to_horizontal_edge(board, -1,  1, 5)
    if direction_input == 'w':
        move_to_vertical_edge(board, 1, 0, len(board))
        sum_numbers_vertical(board, 1, 0, len(board)-1)
        move_to_vertical_edge(board, 1, 0, len(board))
    if direction_input == 's':
        move_to_vertical_edge(board, -1, 1, len(board)+1)
        sum_numbers_vertical(board, -1, 1, 0)
        move_to_vertical_edge(board, -1, 1, len(board) + 1)
    return board


def is_lose(board):
    free_rows = 0
    for row in board:
        if '0' in row:
            free_rows += 1
    if (can_be_sum_horizontal(board, 1, 4) or can_be_sum_horizontal(board, -1, 5) or
            can_be_sum_vertical(board, 1, 0, len(board)-1) or can_be_sum_vertical(board, -1, 1, 0)):
        return False
    if free_rows == 0:
        return True
    return False


def is_winning(board):
    for row in board:
        if '2048' in row:
            return True


def game_2048():
    game_on = True
    board = [['2', '0', '0', '0'], ['2', '0', '0', '0'], ['2', '0', '0', '0'], ['2', '4', '8', '2']]
    print_board(board)
    while game_on:
        direction_input = get_valid_direction()
        old_board = str(board)
        new_board = str(move(direction_input, board))
        if old_board != new_board:
            add_random_number(board, 80)
        print_board(board)
        if is_winning(board):
            game_on = False
            print("You win!")
        if is_lose(board):
            game_on = False
            print("You lose!")


if __name__ == '__main__':
    game_2048()
