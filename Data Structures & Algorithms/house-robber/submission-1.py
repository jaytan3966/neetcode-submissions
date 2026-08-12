class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0]*n
        greatest = float('-inf')
        for i in range(n):
            if i == 0 or i == 1:
                if i == 0: dp[i] = nums[0]
                if i == 1: dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            
            if dp[i]>greatest: greatest = dp[i]
        return greatest