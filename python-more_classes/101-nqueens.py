#!/usr/bin/python3
"""
Solves the N Queens problem.
Usage:
    ./101-nqueens.py N
"""

import sys


def is_safe(board, row, col):
    """
    Check if a queen can be safely placed at (row, col).
    """
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(board, row, n):
    """
    Backtracking function to solve the N Queens problem.
    """
    if row == n:
        solution = []
        for r in range(n):
            solution.append([r, board[r]])
        print(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, n)


def validate_args():
    """
    Validate command-line arguments.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


if __name__ == "__main__":
    n = validate_args()
    board = [-1] * n
    solve(board, 0, n)
