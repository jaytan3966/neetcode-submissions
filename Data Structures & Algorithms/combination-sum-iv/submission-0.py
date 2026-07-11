class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def dfs(total):

            if total == target:
                return 1
            
            if total > target:
                return 0
            
            if total in memo: return memo[total]
            
            ans = 0
            for num in nums:
                ans += dfs(total+num)

            return ans

        return dfs(0)