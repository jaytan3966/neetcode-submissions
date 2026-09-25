class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0

        cur_prod = 1
        n = len(nums)

        ans = 0
        for r in range(n):
            cur_prod*=nums[r]

            while l<r and cur_prod >= k:
                cur_prod/=nums[l]
                l+=1
            if cur_prod < k:
                ans+=(r-l+1)

        return ans
        
