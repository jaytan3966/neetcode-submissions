class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        if s in wordDict: return True

        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for l in range(n):
            for r in range(l, n):
                if s[l:r+1] in wordDict:
                    dp[r+1] = dp[l] or dp[r+1]
        return dp[n]
