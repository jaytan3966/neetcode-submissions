class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n
        for i in range(n):
            for j in range(0, i):
                prefix[i]*=nums[j]
            for k in range (i+1, n):
                prefix[i]*=nums[k]
        ans = [0]*n
        for i in range(n):
            ans[i] = prefix[i]*suffix[i]
        return ans

