class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        cur = 0

        for i in range(n):
            if i>0:
                if nums[i]<=nums[i-1]:
                    ans = max(ans, cur)
                    cur = 0
                cur+=nums[i]
            else:
                cur = nums[i]
        return max(ans, cur)
            

        