class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        ans = 1
        for num in nums:
            if num+1 in seen:
                continue
            n = num
            cur = 1
            while n-1 in seen:
                cur+=1
                n-=1
            ans = max(cur, ans)
        return ans
            