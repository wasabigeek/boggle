import os
from functools import reduce

from flask import Flask, session, render_template, request, redirect, url_for

from helpers import check_word, get_board, get_from_session_or_init


app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']


@app.route('/', methods=['GET'])
def board():
    """Render template for user to play, handle submitted words."""

    if 'board' in session:
        board = session['board']
    else:
        board = get_board()
        session['board'] = board

    words = get_from_session_or_init(session, 'words', [])
    score = reduce(lambda x, y: x + len(y), words, 0)

    return render_template(
        'app.html',
        board=board,
        words=words,
        current_word=get_from_session_or_init(session, 'current_word', ''),
        is_valid=get_from_session_or_init(session, 'is_valid', False),
        message=get_from_session_or_init(session, 'message', ''),
        score=score,
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

    word = request.form['word'].upper()
    words = get_from_session_or_init(session, 'words', [])

    checked_word_obj = check_word(word, words, board)

    session['current_word'] = word
    session['is_valid'] = checked_word_obj['is_valid']
    session['message'] = checked_word_obj['message']
    if checked_word_obj['is_valid']:
        session['words'].append(word)
        session.modified = True

    return redirect(url_for('board'))


@app.route('/clear', methods=['GET'])
def clear():
    """
    Resets the session e.g. found words
    """

    session.pop('board', None)
    session.pop('current_word', None)
    session.pop('words', None)
    session.modified = True

    return redirect(url_for('board'))


@app.route('/instructions', methods=['GET'])
def instructions():
    return render_template('instructions.html')
