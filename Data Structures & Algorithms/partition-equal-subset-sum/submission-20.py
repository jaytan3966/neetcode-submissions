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
            if (i,cur) in include: return include[(i,cur)]

            include[(i,cur)] = dfs(i+1, cur) or dfs(i+1, cur+nums[i])

            return include[(i,cur)]

        return dfs(0, 0)

        

