def tic_tac_win(board: list[list[str]], player: str) -> bool:
    n = len(board)
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Cols
    for c in range(n):
        if all(board[r][c] == player for r in range(n)):
            return True
    # Diags
    if all(board[i][i] == player for i in range(n)):
        return True
    if all(board[i][n-1-i] == player for i in range(n)):
        return True
    return False