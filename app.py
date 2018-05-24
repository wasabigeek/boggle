from flask import Flask, render_template, request


from helpers import get_board, has_next_letter, check_dictionary


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def board():
    """Render template for user to play, handle submitted words."""
    board = get_board()

    if request.method == "POST":
        word = request.form['word']
        is_valid = check_word(word)
        return render_template('app.html', board=board, word=word, is_valid=is_valid)
    else:
        return render_template('app.html', board=board)


def check_word(word):
    """
    Given a word, check if:
    - (1) it can be formed on the board,
    - (2) it can be found in the dictionary
    If both conditions are satisfied, return True.
    """
    board = get_board()
    # First, check if word can be formed on the board
    possible_starts = list(filter(lambda x: x[1] in [word[0], "*"], board))
    for start in possible_starts:
        has_word = has_next_letter(board, start, word[1:])
        # If word is on the board, check if it is in dictionary
        if has_word:
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
            print(f"You found {word}!" if check_word(word) else "Oops! Not a valid word.")
        else:
            playing = False

        print()
