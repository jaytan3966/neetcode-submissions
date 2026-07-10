class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for r in range(n):
            for l in range(r):
                if s[l:r+1] in wordDict:
                    dp[r+1] = dp[l] or dp[r+1]
        print(dp)
        return dp[n]
