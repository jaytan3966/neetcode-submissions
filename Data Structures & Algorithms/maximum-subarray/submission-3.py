class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        cur = 0

        n = len(nums)

        for r in range(n):
            cur+=nums[r]

            ans = max(ans, cur)
            if cur<0:
                cur = 0
        return ans