class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]

        for i in range(len(nums)):
            if nums[i] == target and ans[0] == -1:
                ans[0] = i
            if nums[i] == target and ans[0] != -1:
                ans[1] = i
                
        return ans