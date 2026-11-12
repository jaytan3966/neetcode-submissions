class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        seen = set()
        dp2, dp3, dp5 = 0, 0, 0

        for i in range(1, n):
            two, three, five = dp[dp2]*2, dp[dp3]*3, dp[dp5]*5

            dp[i] = min(two, three, five)
            seen.add(dp[i])

            if dp[i] == two:
                dp2+=1
            if dp[i] == three:
                dp3+=1
            if dp[i] == five:
                dp5+=1
        return dp[n-1]
