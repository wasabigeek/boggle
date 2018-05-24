def check_dictionary(word, dictionary_path="dictionary.txt"):
    """
    Check if word can be found in dictionary.
    Returns Boolean.
    """
    with open(dictionary_path, "r") as f:
        dictionary = f.read().split('\n')
        if word.lower() in dictionary:
            return True
        else:
            return False


def check_word_is_formable(word, board):
    """
    Check if word can be formed from a tile on the board.
    Returns Boolean.
    """
    possible_starts = list(filter(lambda x: x[1] in [word[0], "*"], board))
    for start in possible_starts:
        has_word = check_word_is_formable_from_tile(board, start, word[1:])
        if has_word:
            return True

    return False


def check_word(word, found_words, board):
    if word in found_words:
        return {
            "is_valid": False,
            "message": "This word has already been found."
        }

    if not check_word_is_formable(word, board):
        return {
            "is_valid": False,
            "message": "Cannot find this word on the board."
        }

    if not check_dictionary(word):
        return {
            "is_valid": False,
            "message": "Cannot find this word in the dictionary."
        }

    return {
        "is_valid": True,
        "message": "You found a word!"
    }


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


def get_from_session_or_init(session, param, default):
    if param in session:
        return session[param]
    else:
        value = default
        session[param] = value
        return value


def check_word_is_formable_from_tile(board, tile, remaining_word):
    """
    Given a tile and the remaining letters of the word,
    check if adjacent tiles have the next letter and
    repeat recursively until the word is complete or invalid.
    """
    if len(remaining_word) == 0:
        return True

    adjacent_indexes = get_adjacent_indexes(tile[0])

    # loop through adjacent tiles to find match for next letter
    for i in adjacent_indexes:
        adjacent = board[i]
        if adjacent[1] in remaining_word[0] or adjacent[1] == "*":
            can_form_remaining = check_word_is_formable_from_tile(
                board, board[i], remaining_word[1:]
            )
            # only break the loop if the whole word can be formed
            # else may prematurely miss a word (e.g. BEAK in TestBoard.txt)
            if can_form_remaining:
                return True

    return False
