from app import check_word


def test_check_horizontal_word():
    assert check_word("TAP")


def test_word_with_asterisk():
    assert check_word("BOSS")


def test_check_invalid_word():
    assert not check_word("DATE")
