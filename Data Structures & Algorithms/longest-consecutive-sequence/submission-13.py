class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 1

        for num in nums:
            targ = num
            cnt = 1
            while targ-1 in seen:
                targ+=1
                ans = max(ans, cnt)
                cnt+=1
        return ans