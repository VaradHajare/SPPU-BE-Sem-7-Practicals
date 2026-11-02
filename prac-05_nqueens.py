# n-Queens with first queen already placed (Backtracking)

n = int(input("Enter n: "))
fr = int(input("Row of first queen (1 to n): ")) - 1
fc = int(input("Column of first queen (1 to n): ")) - 1

board = [[0] * n for i in range(n)]
board[fr][fc] = 1                      # place the first queen


def is_safe(row, col):
    # check against every queen already on the board
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                if r == row or c == col or abs(r - row) == abs(c - col):
                    return False
    return True


def solve(row):
    if row == n:                       # all rows done
        return True
    if row == fr:                      # first queen is already in this row
        return solve(row + 1)
    for col in range(n):
        if is_safe(row, col):
            board[row][col] = 1        # place queen
            if solve(row + 1):
                return True
            board[row][col] = 0        # backtrack
    return False


if solve(0):
    print("\nSolution:")
    for row in board:
        print(*row)
else:
    print("\nNo solution possible")