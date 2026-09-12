class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        e = len(s3)
        if n+m != e: return False

        memo = {}

        def dfs(i, j):
            if i+j==e:
                return True

            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = False

            if i<n and s1[i] == s3[i+j]:
                memo[(i, j)] = memo[(i, j)] or dfs(i+1, j)
            if j<m and s2[j] == s3[i+j]:
                memo[(i, j)] = memo[(i, j)] or dfs(i, j+1)
            
            return memo[(i, j)]
        return dfs(0,0)