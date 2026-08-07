class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()

        def dfs(r,c):
            if not (0<=r<n and 0<=c<m): return
            if board[r][c] == 'X': return
            if r==n-1 or c == m-1: return

            board[r][c] = 'X'
            visited.add((r,c))
            for y,x in dirs:
                if (r+y,c+x) not in visited:
                    dfs(r+y,c+x)

        for r in range(n):
            for c in range(m):
                if (r,c) not in visited and board[r][c] == 'O': dfs(r,c)
