class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)<2:
            return len(nums)
        nums.sort()
        i, j = 0, 1
        longest = 1
        while j<len(nums):
            if nums[j]-nums[j-1] != 1:
                i+=1
            else:
                longest = max(longest, j-i+1)
            j+=1
        return longest