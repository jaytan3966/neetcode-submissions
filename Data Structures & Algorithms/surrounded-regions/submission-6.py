class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0, -1)]
        invalid = set()
        seen = set()

        def dfs(r,c):
            if not (0<=r<n and 0<=c<m):
                return
            if board[r][c] == 'X':
                return
            if (r,c) in seen:
                return

            invalid.add((r,c))
            seen.add((r,c))
            for y, x in dirs:
                dfs(r+y,c+x)
        
        rows = [0, n-1]
        for r in rows:
            for c in range(m):
                dfs(r,c)
        cols = [0, m-1]
        for r in range(n):
            for c in cols:
                dfs(r,c)
        
        for r in range(n):
            for c in range(m):
                if (r,c) not in invalid:
                    board[r][c] = 'X'
            