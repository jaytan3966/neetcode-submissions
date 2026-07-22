class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0

        dp = [0]*(n+1)

        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1
        print(dp)
        return dp[n]


