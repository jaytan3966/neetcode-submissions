class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0

        if len(nums) == 1:
            return 1
        for num in nums:
            targ = num
            cnt = 0
            while targ-1 in seen:
                targ+=1
                cnt+=1
                ans = max(ans, cnt)
        return ans