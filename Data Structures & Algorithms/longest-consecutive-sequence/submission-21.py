class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        seen = set()
        n = len(nums)
        
        ans = 0
        for i in range(n):
            if nums[i] in seen or nums[i]+1 in uniques:
                continue
            cur = nums[i]
            cnt = 0
            while cur in uniques:
                seen.add(cur)
                cnt+=1
                cur-=1
            if cnt>ans: ans = cnt
        return ans