class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[nums[i]]<0: return nums[i]
            nums[i]*=-1
        return -nums[n-1]