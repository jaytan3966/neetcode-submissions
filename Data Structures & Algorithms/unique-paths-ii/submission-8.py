class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m = len(obstacleGrid), len(obstacleGrid[0])

        memo = {}

        def dfs(r,c):
            if not (0<=r<n and 0<=c<m): return 0

            if obstacleGrid[r][c] == 1: return 0

            if r==n-1 and c==m-1:
                return 1
            
            if (r,c) in memo:
                return memo[(r,c)]

            memo[(r,c)] = dfs(r+1, c)+dfs(r, c+1)

            return memo[(r,c)]
        
        return dfs(0,0)
