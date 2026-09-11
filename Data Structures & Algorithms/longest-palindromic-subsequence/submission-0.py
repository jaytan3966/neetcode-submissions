class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        reverse = s[::-1]
        n = len(s)

        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        ans = 0

        for l in range(1, n+1):
            for r in range(1, n+1):
                if s[l-1] == reverse[r-1]:
                    dp[l][r] = 1 + dp[l-1][r-1]
                else:
                    dp[l][r] = max(dp[l-1][r], dp[l][r-1])
                if dp[l][r] > ans: ans = dp[l][r]
        
        return ans