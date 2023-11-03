#!/usr/bin/python3

import sys


def is_safe(board, row, col, n):
    for i in range(col):
        if board[i] == row or board[i] - i == row - col\
                or board[i] + i == row + col:
            return False
    return True


def solve_n_queens_util(board, col, n):
    if col == n:
        print_solution(board, n)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[col] = i
            res = solve_n_queens_util(board, col + 1, n) or res
            board[col] = -1

    return res


def solve_n_queens(n):
    board = [-1 for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")


def print_solution(board, n):
    solution = []
    for i in range(n):
        row = [i, board[i]]
        solution.append(row)

    print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(N)
