class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        subset = []

        def dfs(i):
            nonlocal ans

            if i >= n: 
                ans.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

            return

        dfs(0)
        return ans


