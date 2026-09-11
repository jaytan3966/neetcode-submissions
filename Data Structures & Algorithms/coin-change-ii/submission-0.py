class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        m = amount

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        # dp[i][c] = number of distinct combinations that total to c from the first i coins

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1,n+1):
            for amnt in range(m+1):
                dp[i][amnt] = dp[i-1][amnt]

                if coins[i-1]>amnt: continue

                dp[i][amnt]+=dp[i][amnt-coins[i-1]]
        
        return dp[n][amount]