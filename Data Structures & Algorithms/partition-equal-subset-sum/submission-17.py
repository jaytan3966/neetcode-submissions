class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2: return False

        target = total//2
        n = len(nums)
        include = {}

        def dfs(i, cur):
            if cur == target: return True
            if i == n: return False

            if (i+1, cur) not in include:
                include[(i+1, cur)] = dfs(i+1, cur)
            if (i+1, cur+nums[i]) not in include:
                include[(i+1, cur+nums[i])] = dfs(i+1, cur+nums[i])
            return include[(i+1, cur+nums[i])] or include[(i+1, cur)]

        return dfs(0, 0)

        

