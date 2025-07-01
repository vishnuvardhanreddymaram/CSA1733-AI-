def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):
    # Check this column on upper side
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False

    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solutions.append([r[:] for r in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack

def solve_n_queens(n=8):
    board = [[0]*n for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

# Run and print all solutions
all_solutions = solve_n_queens()

print(f"Total solutions for {len(all_solutions)}-Queens: {len(all_solutions)}\n")
for i, solution in enumerate(all_solutions, 1):
    print(f"Solution {i}:")
    print_board(solution)