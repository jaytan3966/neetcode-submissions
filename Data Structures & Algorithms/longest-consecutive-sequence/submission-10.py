class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:



        nums.sort()
        seen = set()
        i, j, longest, curLongest = 0, 1, 1, 1

        while j<len(nums):
            if nums[j]-nums[j-1] == 1:    
                if nums[j] not in seen:
                    curLongest+=1
                    seen.add(nums[j])
                longest = max(longest, curLongest)
            elif nums[j]-nums[j-1] == 0:
                pass
            else:
                curLongest = 1
                i+=1 
                j = i 
            j+=1
        return longest