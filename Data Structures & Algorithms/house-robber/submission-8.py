class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1: return nums[0]

        dp0 = nums[0]
        dp1 = max(nums[0], nums[1])

        for i in range(2, n):
            op1 = dp0
            op2 = dp1
            dp1 = max(op2, nums[i]+op1)
            dp0 = op2
        
        return dp1