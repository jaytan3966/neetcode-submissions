class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for c in coins:
            for a in range(1, amount+1):
                if c<=a:
                    dp[a] = min(1 + dp[a-c], dp[a])
        return dp[amount] if dp[amount] != float('inf') else -1
