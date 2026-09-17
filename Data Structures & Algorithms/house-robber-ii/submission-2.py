class Solution:
    def rob(self, nums: List[int]) -> int:
        first_half = nums[:-1]
        second_half = nums[1:]

        def greatest_rob(nums):
            n = len(nums)
            if n == 1: return nums[0]

            dp1 = nums[0]
            dp2 = max(nums[0], nums[1])

            for i in range(2, n):
                op1 = dp1
                op2 = dp2
                dp2 = max(nums[i]+op1, op2)
                dp1 = op2
            
            return dp2
        
        return max(greatest_rob(first_half), greatest_rob(second_half))

        