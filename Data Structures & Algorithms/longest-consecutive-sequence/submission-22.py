class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        ans = 0
        for num in nums:
            if num+1 in seen: continue
            cnt = 0
            cur = num

            while cur in seen:
                cnt+=1
                cur-=1
            ans = max(cnt, ans)
        return ans