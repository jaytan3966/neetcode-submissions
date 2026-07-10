class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        if s in wordDict: return True

        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        lengths = {len(w) for w in wordDict}

        for l in range(n):
            if not dp[l]: continue
            for k in lengths:
                if l+k<=n and s[l:l+k] in wordDict:
                    dp[l+k] = True
        return dp[n]
