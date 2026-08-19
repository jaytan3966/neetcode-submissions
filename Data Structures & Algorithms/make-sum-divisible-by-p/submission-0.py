class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        ns = set(nums)
        n = len(nums)

        if total<p: return -1
        if total%p==0: return 0
        if total%p in ns: return 1

        pref = [0]*n
        pref[0] = nums[0]
        for i in range(n):
            pref[i] = nums[i]+pref[i-1]
            print(pref[i], i, n)
            if pref[i]%p==0: return n-(i+1)
            
        return -1