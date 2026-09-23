class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        n, m = len(matrix), len(matrix[0])
        memo = {}

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(r,c):
            if not (0<=r<n and 0<=c<m):
                return 0
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            memo[(r,c)] = 1
            longest = 0
            for y, x in dirs:

                if not (0<=r+y<n and 0<=c+x<m): continue
                
                if matrix[r+y][c+x]<matrix[r][c]:
                    longest = max(longest, dfs(r+y,c+x))
            memo[(r,c)]+=longest

            return memo[(r,c)]
        
        ans = 1
        for r in range(n):
            for c in range(m):
                if (r,c) not in memo:
                    ans = max(ans, dfs(r,c))
        
        return ans
