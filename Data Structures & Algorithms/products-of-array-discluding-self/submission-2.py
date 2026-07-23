class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefArr = [0]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            prefArr[i] = prefix
            prefix*=nums[i]

        postArr = [0]*len(nums)
        postFix = 1
        for i in range(len(nums)-1, -1, -1):
            postArr[i] = postFix
            postFix*=nums[i]
        
        ans = [0]*len(nums)
        for i in range(len(ans)):
            ans[i] = prefArr[i]*postArr[i]
        return ans

