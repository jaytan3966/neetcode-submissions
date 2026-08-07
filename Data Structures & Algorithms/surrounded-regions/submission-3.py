class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        seen = set()

        def dfs(r,c):
            if not 0<=r<n or not 0<=c<m:
                return
            if board[r][c] == 'X' or board[r][c] == 'W':
                return 
            
            found = False
            for y,x in dirs:
                if 0<=r+y<n and 0<=c+x<m:
                    if board[r+y][c+x] == 'O' or board[r+y][c+x] == 'W':
                        seen.add((r,c))
                        found = True
                        break
            if not found:
                board[r][c] == 'W'
            
        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O':
                    dfs(r,c)
        for r,c in seen:
            board[r][c] = 'X'
                    

        