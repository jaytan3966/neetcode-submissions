class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pres = [1] * n
        suffs = [1] * n

        cur = 1

        for i in range(n):
            pres[i]*=cur
            cur*=nums[i]
        
        cur = 1
        for i in range(n-1, -1, -1):
            suffs[i]*=cur
            cur*=nums[i]
        
        return [pres[i]*suffs[i] for i in range(n)]

