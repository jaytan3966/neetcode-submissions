class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 0
        dirs = [(0,1), (-1,0)]

        def dfs(r,c):
            nonlocal ans

            if r>=m or c>=n:
                return

            if (r,c) in seen: return
            if r==m-1 and c == n-1:
                ans+=1
                return
            
            if (r,c) in seen: return

