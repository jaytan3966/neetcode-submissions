class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)<2:
            return len(nums)

        nums.sort()
        seen = set()
        count = Counter(nums)
        i, j, longest = 0, 1, 1

        while j<len(nums):
            if nums[j]-nums[j-1] != 1:    
                i+=1 
            else:
                if nums[j] not in seen:
                    longest = max(longest, j-i+1)
                    seen.add(nums[j])
                else:
                    longest = max(longest, j-i+1-count[nums[j]]+2)
            j+=1
        return longest