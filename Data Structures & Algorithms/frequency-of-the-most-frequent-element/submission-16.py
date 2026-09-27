class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        window_sum = 0
        ans = 1
        n = len(nums)

        for r in range(n):
            window_sum+=nums[r]

            while nums[r] * (r-l+1) - window_sum > k:
                window_sum-=nums[l]
                l+=1
            
            ans = max(ans, r-l+1)
        return ans