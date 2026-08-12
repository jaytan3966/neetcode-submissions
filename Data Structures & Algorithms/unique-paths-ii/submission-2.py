class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m = len(obstacleGrid), len(obstacleGrid[0])
        dirs = [(1,0), (0,1)]
        visited = set()
        ans = 0
        
        def dfs(r,c):
            nonlocal ans
            if not (0<=r<n and 0<=c<m) or (r,c) in visited or obstacleGrid[r][c]: 
                return
            if r == n-1 and c == m-1:
                ans+=1
                return

            visited.add((r,c))

            for y, x in dirs:
                dfs(r+y, c+x)
            visited.remove((r,c))
            return
        dfs(0,0)
        
        return ans
            




