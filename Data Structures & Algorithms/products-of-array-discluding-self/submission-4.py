class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*n
        suff = [0]*n
        ans = [0]*n

        pre = 1
        for l in range(n):
            pref[l] = pre
            pre*=nums[l]
        
        suf = 1
        for r in range(n-1, -1, -1):
            suff[r] = suf
            suf*=nums[r]

        for i in range(n):
            ans[i] = pref[i]*suff[i]
        return ans