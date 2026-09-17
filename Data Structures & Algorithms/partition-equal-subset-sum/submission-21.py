class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total%2: return False

        target = total//2
        n = len(nums)

        def dfs(i, cur_sum):
            if cur_sum == target:
                return True
            
            if i>=n: return False
            
            return dfs(i+1, cur_sum+nums[i]) or dfs(i+1, cur_sum)
        
        return dfs(0,0)