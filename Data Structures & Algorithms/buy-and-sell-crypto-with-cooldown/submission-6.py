class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0 for _ in range(2)] for _ in range(n)]
        # dp[i][True] = max profit on day i buying the stock at i
        # dp[i][False] = max profit on day i not buying the stock

        dp[0][True] = -prices[0]

        for i in range(1, n):
            dp[i][True] = dp[i-1][True]

            if i>=2:
                dp[i][True] = max(dp[i-1][True], -prices[i]+dp[i-2][False])
            else:
                dp[i][True] = max(dp[i-1][True], -prices[i])
                
            dp[i][False] = max(dp[i-1][False], dp[i-1][True] + prices[i])

        return dp[n-1][False]