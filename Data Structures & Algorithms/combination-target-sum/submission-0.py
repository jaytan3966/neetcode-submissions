class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)

        def dfs(i, comb, cur):
            if cur == target:
                ans.append(comb[:])
                return
            if i>= n or cur>target:
                return
            comb.append(nums[i])
            dfs(i, comb, cur+nums[i])
            comb.pop()
            dfs(i+1, comb, cur)
            
        dfs(0, [], 0)
        return ans