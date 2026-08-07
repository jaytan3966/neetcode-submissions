class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O':
                    if r == 0 or c == 0 or r == n-1 or r == m-1: 
                        continue
                    board[r][c] = 'X'

        