class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums: return 0
        
        seen = set(nums)
        ans = 1

        for n in nums:
            count = 1
            if n+1 in seen: continue

            cop = n
            while cop-1 in seen:
                count+=1
                cop-=1
            ans = max(ans, count)
        return ans

