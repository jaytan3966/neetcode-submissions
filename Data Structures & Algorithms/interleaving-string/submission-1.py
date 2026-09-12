class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        e = len(s3)
        if n+m != e: return False

        i, j, k = 0, 0, 0

        def dfs(i, j, k):
            if k==e:
                return True
            
            valid = False
            if i<n and s1[i] == s3[k]:
                valid = valid or dfs(i+1, j, k+1)
            elif j<m and s2[j] == s3[k]:
                valid = valid or dfs(i, j+1, k+1)
            else:
                return False
            
            return valid
        return dfs(0,0,0)