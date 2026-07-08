class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        n = len(nums)

        def dfs(i, comb):
            if i>=n: 
                ans.append(comb[:])
                return

            comb.append(nums[i])
            dfs(i+1, comb)
            comb.pop()

            while i+1<n and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1, comb)
            return
        dfs(0, [])
        return ans 