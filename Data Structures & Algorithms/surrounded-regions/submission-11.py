class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        invalid = set()

        def dfs(r,c):
            if not (0<=r<n and 0<=c<m): return
            if board[r][c] == 'X': return
            if not (r == 0 or c == 0 or r==n-1 or c == m-1): return

            invalid.add((r,c))
            for y,x in dirs:
                if (r+y,c+x) not in invalid:
                    dfs(r+y,c+x)

        for r in range(n):
            dfs(r,0)
            dfs(r,m-1)
        for c in range(m):
            dfs(0,c)
            dfs(n-1,c)
        print(invalid)
        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O' and (r,c) not in invalid: board[r][c] = 'X'
