class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = nums.copy()
        n = len(nums)
        greatest = float('-inf')

        for i in range(1,n):
            dp[i] = max(dp[i-1]*nums[i], dp[i])
            if dp[i] > greatest: greatest = dp[i]

        return greatest