class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        allNums = set()
        ans = 1

        for num in seen:
            if num in allNums:
                continue
            if num-1 not in seen:
                cnt = 0
                cur = num
                while cur in seen and cur not in allNums:
                    cnt+=1
                    allNums.add(cur)
                    cur+=1
                ans = max(ans, cnt)
        return ans