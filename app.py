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
        has_word = has_next_letter(board, start, word[1:])
        print(has_word)
        if has_word:
            return True

    return False


def has_next_letter(board, tile, remaining_word):
    if len(remaining_word) == 0:
        return True

    # find the indexes of adjacent tiles
    row = int(tile[0] / 4)
    col = tile[0] % 4

    adjacent_indexes = []
    if row > 0:
        adjacent_indexes.append(tile[0] - 4)  # top
    if row < 3:
        adjacent_indexes.append(tile[0] + 4)  # bottom
    if col > 0:
        adjacent_indexes.append(tile[0] - 1)  # left
    if col < 3:
        adjacent_indexes.append(tile[0] + 1)  # right
    if row > 0 and col > 0:
        adjacent_indexes.append(tile[0] - 5)  # top-left
    if row > 0 and col < 3:
        adjacent_indexes.append(tile[0] - 3)  # top-right
    if row < 3 and col > 0:
        adjacent_indexes.append(tile[0] + 3)  # bottom-left
    if row < 3 and col < 3:
        adjacent_indexes.append(tile[0] + 5)  # bottom-right

    for i in adjacent_indexes:
        adjacent = board[i]
        if adjacent and (adjacent[1] in remaining_word[0] or adjacent[1] == "*"):
            return has_next_letter(board, board[i], remaining_word[1:])

    return False


check_word("TAP")
