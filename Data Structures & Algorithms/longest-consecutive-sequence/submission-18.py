class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allNums = set(nums)
        seen = set()
        ans = 0
        
        for num in nums:
            if num not in seen:
                cnt = 1
                while num+1 in allNums:
                    cnt+=1
                    seen.add(num)
                    num+=1
                ans = max(ans, cnt)
        return ans