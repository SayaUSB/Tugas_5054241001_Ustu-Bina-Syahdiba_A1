from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []

        def is_safe(board, row, col, n):
            for i in range(col):
                if board[row][i] == 'Q':
                    return False
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            for i, j in zip(range(row, n, 1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            return True

        def backtrack(board, col):
            if col == n:
                result.append([''.join(row) for row in board])
                return

            for i in range(n):
                if is_safe(board, i, col, n):
                    board[i][col] = 'Q'
                    backtrack(board, col + 1)
                    board[i][col] = '.'

        backtrack(board, 0)
        return result