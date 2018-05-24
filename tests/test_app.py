from helpers import get_board, check_word


board = get_board()


def test_check_horizontal_word():
    assert check_word("TAP", board)


def test_word_with_asterisk():
    assert check_word("BOSS", board)


def test_word_with_diagonal():
    assert check_word("BEAK", board)
    assert check_word("BOAR", board)
    assert check_word("BIRD", board)


def test_letters_not_adjacent():
    assert not check_word("DATE", board)


def test_invalid_word():
    assert not check_word("ALUGE", board)
