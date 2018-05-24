from helpers import get_board, check_word_is_formable


board = get_board()


def test_check_horizontal_word():
    assert check_word_is_formable("TAP", board)


def test_word_with_asterisk():
    assert check_word_is_formable("BOSS", board)


def test_word_with_diagonal():
    assert check_word_is_formable("BEAK", board)
    assert check_word_is_formable("BOAR", board)
    assert check_word_is_formable("BIRD", board)


def test_letters_not_adjacent():
    assert not check_word_is_formable("DATE", board)


def test_invalid_word():
    assert not check_word_is_formable("ALUGE", board)
