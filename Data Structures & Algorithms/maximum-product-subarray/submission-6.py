class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        greatest = nums[0]

        for num in nums:
            cur = curMax*num
            curMax = max(cur, curMin*num, num)
            curMin = min(curMin*num, cur, num)
            greatest = curMax if curMax>greatest else greatest

        return greatest