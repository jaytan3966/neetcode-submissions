class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        if n<m:
            return 0

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for r in range(n+1):
            dp[r][0] = 1

        for r in range(1, n+1):
            for c in range(1, m+1):
                dp[r][c] = dp[r-1][c]
                if s[r-1] == t[c-1]:
                    dp[r][c] += dp[r-1][c-1]

        return dp[n][m]
