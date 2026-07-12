class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allNums = set(nums)
        seen = set()
        ans = 0
        for num in nums:
            if num not in seen:
                curLen = 1
                while num+1 in allNums:
                    curLen+=1
                    seen.add(num)
                    num+=1
                ans = max(ans, curLen)
        return ans