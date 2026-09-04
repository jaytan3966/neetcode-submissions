class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r,c):
            if not (0<=r<n and 0<=c<m) or grid[r][c] != 1:
                return
            
            grid[r][c] = 0

            for y, x in dirs:
                dfs(r+y, c+x)
            return
        
        for r in range(n):
            dfs(r, 0)
            dfs(r, m-1)
        for c in range(1, m-1):
            dfs(0, c)
            dfs(n-1, c)
        
        count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1: count+=1
        return count
