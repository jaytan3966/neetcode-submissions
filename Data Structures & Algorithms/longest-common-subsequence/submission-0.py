class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n, m = len(text1), len(text2)
        
        ans = [[0 for _ in range(m+1)] for _ in range(n+1)]

        greatest = 0

        for r in range(1, n+1):
            for c in range(1, m+1):
                if text1[r-1]==text2[c-1]:
                    ans[r-1][c-1] = 1+ans[r-2][c-2]
                else:
                    ans[r-1][c-1] = max(ans[r-2][c-1], ans[r-1][c-2])
                greatest = max(ans[r-1][c-1], greatest)

        return greatest

        
