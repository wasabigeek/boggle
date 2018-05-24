def get_board(path='TestBoard.txt'):
    with open(path, 'r') as f:
        # convert board to a list of tiles
        board = f.read().split(', ')
        return list(enumerate(board))


def show_board():
    board = get_board()
    for index, letter in board:
        # new row on every fourth tile
        end = "\n" if (index + 1) % 4 == 0 else " "
        print(letter, end=end)


show_board()


def check_word(word):
    board = get_board()
    # find start of word
    possible_starts = list(filter(lambda x: x[1] in [word[0], "*"], board))
    for start in possible_starts:
        has_next_letter(board, start)


def has_next_letter(board, tile):
    adjacent_indexes = [
        tile[0] - 4,  # top
        tile[0] + 4,  # bottom
        tile[0] - 1,  # left
        tile[0] + 1,  # right
    ]
    adjacent_tiles = [board[i] for i in adjacent_indexes if i >= 0 and i < 16]
    print(adjacent_tiles)


check_word("TAPE")
