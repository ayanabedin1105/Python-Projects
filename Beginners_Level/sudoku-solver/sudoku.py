def is_valid(board, row, col, num):
    """
    Check if it's valid to place the number `num` at position (row, col) on the board.
    """
    # Check the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check the 3x3 sub-grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using backtracking.
    """
    empty_cell = find_empty(board)
    if not empty_cell:
        return True  # No empty cells, puzzle solved!
    row, col = empty_cell

    for num in range(1, 10):  # Try numbers 1 through 9
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):  # Recursively try to solve the rest
                return True

            board[row][col] = 0  # Backtrack

    return False  # Trigger backtracking

def find_empty(board):
    """
    Find the next empty cell (with value 0) on the board.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_board(board):
    """
    Print the Sudoku board.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku puzzle
if solve_sudoku(sudoku_board):
    print("Sudoku puzzle solved:")
    print_board(sudoku_board)
else:
    print("No solution exists for the given Sudoku puzzle.")
