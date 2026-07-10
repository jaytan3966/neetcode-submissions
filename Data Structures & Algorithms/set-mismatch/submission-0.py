class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        seen = set()

        for num in nums:
            if num in seen:
                ans.append(num)
                ans.append(num+1)
                break
            seen.add(num)
        return ans