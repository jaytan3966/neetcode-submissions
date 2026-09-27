class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, l = len(s1), len(s2), len(s3)

        def dfs(i,j,k):
            if not ((i<n or j<m) and k<l):
                return i == n and j == m and k == l

            if not ((i<n and s1[i] == s3[k]) or (j<m and s2[j] == s3[k])):
                return False

            if i<n and s1[i] == s3[k]:
                return dfs(i+1, j, k+1)
            elif j<m and s2[j] == s3[k]:
                return dfs(i, j+1, k+1)
            
            return False
        
        return dfs(0,0,0)


