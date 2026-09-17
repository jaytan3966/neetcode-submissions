class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total%2: return False

        target = total//2
        n = len(nums)
        seen = {}

        def dfs(i, cur_sum):
            if cur_sum == target:
                return True
            if cur_sum in seen:
                return seen[cur_sum]
            
            if i>=n: return False

            seen[cur_sum] = dfs(i+1, cur_sum+nums[i]) or dfs(i+1, cur_sum)
            
            return seen[cur_sum]
        
        return dfs(0,0)