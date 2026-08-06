class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        greatest = nums[0]

        for num in nums:
            include = curMax*num
            curMax = max(curMax*num, curMin*num, num)
            curMin = min(curMin*num, include, num)
            greatest = curMax if curMax>greatest else greatest

        return greatest