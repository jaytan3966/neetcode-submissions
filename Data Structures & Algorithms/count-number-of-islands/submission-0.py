class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1, 0)]

        def dfs (r, c):
            if not (0<=r<n and 0<=c<m):
                return
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            for y,x in dirs:
                dfs(r+y, c+x)
            return
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    ans+=1
                    dfs(r,c)
        return ans
