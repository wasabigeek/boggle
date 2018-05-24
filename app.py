def get_board(path='TestBoard.txt'):
    with open(path, 'r') as f:
        # convert board to a list of tiles
        board = f.read().split(', ')
        return list(enumerate(board))


def show_board():
    board = get_board()
    for index, letter in board:
        # new row on every fourth tile
        end = "\n" if (index + 1) % 4 == 0 else " "
        print(letter, end=end)


show_board()
