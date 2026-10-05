class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]

        dp[0][True] = -prices[0]
        dp[0][False] = 0

        for i in range(1,n):
            dp[i][True] = max(-prices[i]+dp[i-1][False], dp[i-1][True])

            dp[i][False] = max(prices[i]+dp[i-1][True], dp[i-1][False])
        
        return max(dp[n-1][False], dp[n-1][True])