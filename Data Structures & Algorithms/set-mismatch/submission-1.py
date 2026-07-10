class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        seen = set()
        n = len(nums)
        for i in range(n):
            if i+1 in seen:
                ans.append(i+1)
                ans.append(i+1+1)
                break
            seen.add(i+1)
        return ans