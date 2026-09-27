class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, l = len(s1), len(s2), len(s3)
        memo = {}

        def dfs(i,j):
            if i+j==l:
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            left, right = False, False

            if i<n and s1[i] == s3[i+j]:
                left =  dfs(i+1, j)
            if j<m and s2[j] == s3[i+j]:
                right =  dfs(i, j+1)

            memo[(i, j)] = left or right

            return memo[(i, j)]
        
        return dfs(0,0)


