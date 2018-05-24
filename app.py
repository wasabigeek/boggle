from helpers import get_board, has_next_letter, check_dictionary


def show_board():
    board = get_board()
    for index, letter in board:
        # new row on every fourth tile
        end = "\n" if (index + 1) % 4 == 0 else " "
        print(letter, end=end)


def check_word(word):
    board = get_board()
    # check if word can be formed on the board
    possible_starts = list(filter(lambda x: x[1] in [word[0], "*"], board))
    for start in possible_starts:
        has_word = has_next_letter(board, start, word[1:])
        if has_word:
            # check if word is in dictionary
            return check_dictionary(word)

    return False


if __name__ == "__main__":
    print("Current Board:")
    show_board()
    print()

    playing = True
    while playing:
        print("What would you like to do?")
        print("[1] Display the board")
        print("[2] Check a word")
        print("[3] Exit")
        action = int(input("--> "))

        if action == 1:
            show_board()
        elif action == 2:
            print("What word would you like to check?")
            word = input("--> ")
            print(check_word(word))
        else:
            playing = False

        print()
