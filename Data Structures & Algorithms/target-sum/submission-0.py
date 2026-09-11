class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)

        def dfs(i, curSum):
            nonlocal ans

            if i == n:
                if curSum == target:
                    ans+=1
                return
            
            dfs(i+1, curSum+nums[i])
            dfs(i+1, curSum-nums[i])
            
            return
        dfs(0, 0)

        return ans
            

