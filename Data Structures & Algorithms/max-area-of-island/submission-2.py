class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1, 0)]

        def dfs(r, c, count):
            if not (0<=r<n and 0<=c<m):
                return count
            if grid[r][c] == 0:
                return count
            
            grid[r][c] = 0
            count+=1

            for y,x in dirs:
                count = dfs(r+y, c+x, count)
            return count
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    count = 0
                    ans = max(dfs(r,c, count), ans)

        return ans