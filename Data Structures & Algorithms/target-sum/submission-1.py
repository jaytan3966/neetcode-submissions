class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(i, curSum):
            if i == n:
                return curSum == target
            if (i, curSum) in memo:
                return memo[(i, curSum)]
            
            memo[(i, curSum)] = dfs(i+1, curSum+nums[i]) + dfs(i+1, curSum-nums[i])
            
            return memo[(i, curSum)]

        return dfs(0, 0)
            

