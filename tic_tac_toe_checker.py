def is_solved(board: list[list]):
    """
    Evaluate the state of a tic-tac-toe board.

    The board is a 3×3 list of lists. Each element is 0 for an empty
    tile, 1 for player one, or 2 for player two.

    Return the winning player number if either player has three marks
    in a row.
    Return −1 if the game is unfinished and at least one tile is empty.
    Return 0 if all tiles are filled and neither player has won.

    :param board: A 3x3 list of lists representing the board.
    :return: An integer describing the game state.
    """
    
    marks = [1, 2]
    columns = [
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        ]
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
        ]
    for mark in marks:
        if [mark, mark, mark] in board + columns + diagonals:
            return mark
    if 0 in board[0] or 0 in board[1] or 0 in board[2]:
        return -1
    return 0
