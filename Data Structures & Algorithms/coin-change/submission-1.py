class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount != 0 and min(coins)>amount: return -1

        n = len(coins)

        dp = [[float('inf') for _ in range(amount+1)] for _ in range(n)]
        
        for r in range(n):
            dp[r][0] = 0

        for i in range(n):
            for a in range(1, amount+1):
                dp[i][a] = min(1+dp[i][a-coins[i]], 1+dp[i-1][a-coins[i]], dp[i-1][a])
        ans = float('inf')

        for r in range(n):
            if dp[r][amount]<ans: ans = dp[r][amount]
        print(dp)
        return -1 if ans == float('inf') else ans
