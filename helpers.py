def get_adjacent_indexes(index):
    """Given a tile's index (0 - 15), return a list of adjacent tile indexes"""
    row = int(index / 4)
    col = index % 4

    adjacent_indexes = []
    if row > 0:
        adjacent_indexes.append(index - 4)  # top
    if row < 3:
        adjacent_indexes.append(index + 4)  # bottom
    if col > 0:
        adjacent_indexes.append(index - 1)  # left
    if col < 3:
        adjacent_indexes.append(index + 1)  # right
    if row > 0 and col > 0:
        adjacent_indexes.append(index - 5)  # top-left
    if row > 0 and col < 3:
        adjacent_indexes.append(index - 3)  # top-right
    if row < 3 and col > 0:
        adjacent_indexes.append(index + 3)  # bottom-left
    if row < 3 and col < 3:
        adjacent_indexes.append(index + 5)  # bottom-right

    return adjacent_indexes


def get_board(path='TestBoard.txt'):
    """
    Given a txt representation of a board,
    convert to a list of tuples (index, letter)
    """
    with open(path, 'r') as f:
        # convert board to a list of tiles
        board = f.read().split(', ')
        return list(enumerate(board))


def has_next_letter(board, tile, remaining_word):
    """
    Given a tile and the remaining letters of the word,
    check if adjacent tiles have the next letter and
    repeat recursively until the word is complete or invalid.
    """
    if len(remaining_word) == 0:
        return True

    adjacent_indexes = get_adjacent_indexes(tile[0])

    for i in adjacent_indexes:
        adjacent = board[i]
        if adjacent[1] in remaining_word[0] or adjacent[1] == "*":
            return has_next_letter(board, board[i], remaining_word[1:])

    # TODO: Check word is valid in dictionary

    return False
