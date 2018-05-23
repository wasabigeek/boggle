def show_board():
    with open('TestBoard.txt', 'r') as f:
        # convert board to a list of tiles
        board = f.read().split(', ')
        # print out tiles in rows of 4
        for index, tile in enumerate(board, 1):
            # new row on every fourth tile
            end = "\n" if index % 4 == 0 else " "
            print(tile, end=end)
