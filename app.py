import os

from flask import Flask, session, render_template, request, redirect, url_for

from helpers import get_board, check_word, get_from_session_or_init


app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']


@app.route('/', methods=['GET', 'POST'])
def board():
    """Render template for user to play, handle submitted words."""

    if 'board' in session:
        board = session['board']
    else:
        board = get_board()
        session['board'] = board

    words = get_from_session_or_init(session, 'words', [])
    current_word = get_from_session_or_init(session, 'current_word', '')
    is_valid = get_from_session_or_init(session, 'is_valid', False)

    return render_template(
        'app.html',
        board=board,
        words=words,
        current_word=current_word,
        is_valid=is_valid,
    )


@app.route('/check', methods=['POST'])
def check():
    """
    Given a word, check if:
    - (1) it can be formed on the board,
    - (2) it can be found in the dictionary
    If both conditions are satisfied, return True.
    """
    if 'board' in session:
        board = session['board']
    else:
        board = get_board()
        session['board'] = board

    word = request.form['word']

    is_valid = check_word(word, board)

    session['current_word'] = word
    session['is_valid'] = is_valid
    if is_valid:
        session['words'].append(word)
        session.modified = True

    return redirect(url_for('board'))
