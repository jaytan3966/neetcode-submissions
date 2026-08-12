class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m = len(obstacleGrid), len(obstacleGrid[0])

        ans = 0

        def dfs(r,c):
            nonlocal ans
            
            if not (0<=r<n and 0<=c<m): return

            if obstacleGrid[r][c] == 1: return

            if r==n-1 and c==m-1:
                ans+=1
                return
            dfs(r+1, c)
            dfs(r, c+1)
            return
        dfs(0,0)
        return ans
