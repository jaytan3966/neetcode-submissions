class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        first = nums[:-1]
        second = nums[1:]

        dp1 = [0]*(n-1)
        dp2 = [0]*(n-1)
        greatest = float('-inf')

        for i in range(n-1):
            
            if i == 0 or i == 1:
                if i == 0: dp1[i] = nums[i]
                if i == 1: dp1[i] = max(nums[i], dp1[i-1])

            else:
                dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
            if dp1[i]>greatest: greatest = dp1[i]

        for i in range(1, n):
            
            if i == 0 or i == 1:
                if i == 1: dp2[i-1] = nums[i]
                if i == 2: dp2[i-1] = max(nums[i], dp2[i-2])

            else:
                dp2[i-1] = max(dp2[i-3]+nums[i], dp2[i-2])
            print(dp2)
            if dp2[i-1]>greatest: greatest = dp2[i-1]
        
        return greatest