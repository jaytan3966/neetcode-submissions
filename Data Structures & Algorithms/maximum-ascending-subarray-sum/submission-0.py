class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        cur = 0

        for i in range(n):
            if i>0:
                if nums[i]>nums[i-1]:
                    cur+=nums[i]
                    ans = max(ans, cur)
                else:
                    ans = max(ans, cur)
                    cur = nums[i]
            else:
                cur = nums[i]
        return max(ans, cur)
            

        