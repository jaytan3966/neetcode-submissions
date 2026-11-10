class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        dirs = [(0,1), (1,0)]

        def dfs(r, c):
            if not (0<=r<m and 0<=c<n):
                return 0
            if r==m-1 and c==n-1:
                return 1
            if (r,c) in memo:
                return memo[(r,c)]
            
            count = 0
            for y, x in dirs:
                count += dfs(r+y, c+x)
            
            memo[(r,c)] = count

            return count
        
        return dfs(0,0)

            


            