class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dirs = [(0,1), (1,0)]

        memo = {}
        
        def dfs(r,c):
            if not (0<=r<m and 0<=c<n):
                return 0
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            if r == m-1 and c == n-1:
                return 1
            
            memo[(r,c)] = dfs(r,c+1) + dfs(r+1, c)
            
            return memo[(r,c)]
        
        return dfs(0,0)
        
