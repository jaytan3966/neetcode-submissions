class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def dfs(i, subset):
            if i>=n:
                ans.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            dfs(i+1, subset)
        dfs(0, [])
        return ans
