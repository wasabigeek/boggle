from app import check_word


def test_check_horizontal_word():
    assert check_word("TAP")


def test_word_with_asterisk():
    assert check_word("BOSS")


def test_word_with_diagonal():
    assert check_word("BEAK")
    assert check_word("BOAR")
    assert check_word("BIRD")


def test_letters_not_adjacent():
    assert not check_word("DATE")


def test_invalid_word():
    assert not check_word("ALUGE")
