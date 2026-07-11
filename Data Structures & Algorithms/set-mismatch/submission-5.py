class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [-1, -1]
        counts = Counter(nums)
        for i in range(n):
            if counts[i+1] == 0:
                ans[1] = i+1
            if counts[i+1] == 2:
                ans[0] = i+1
        return ans
            