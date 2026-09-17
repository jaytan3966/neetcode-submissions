class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [[float('inf') for _ in range(amount+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0
        
        for a in range(amount+1):
            for i in range(1, n+1):
                if coins[i-1]<=a:
                    dp[i][a] = min(1+dp[i][a-coins[i-1]], dp[i-1][a])
                else:
                    dp[i][a] = dp[i-1][a]

        return dp[n][amount] if dp[n][amount]!=float('inf') else -1