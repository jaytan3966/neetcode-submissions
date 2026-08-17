class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validColumn = defaultdict(set)
        validRow = defaultdict(set)
        validBox = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    if board[r][c] in validColumn[c] or board[r][c] in validRow[r] or board[r][c] in validBox[(r//3,c//3)]: return False
                    validColumn[c].add(board[r][c])
                    validRow[r].add(board[r][c])
                    validBox[(r//3,c//3)].add(board[r][c])
        return True