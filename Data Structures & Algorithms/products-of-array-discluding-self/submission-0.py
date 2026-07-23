class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []

        for i in range(len(nums)):
            if i == 0:
                ans.append(math.prod(nums[1:]))
            else:
                ans.append(math.prod(nums[:i])*math.prod(nums[i+1:]))
        return ans