class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)

        def dfs(i, comb, t):
            if t == 0: 
                ans.append(comb[:])
                return
            if i < 0 or t<0: return

            comb.append(nums[i])
            dfs(i,comb,t-nums[i])
            comb.pop()
            dfs(i-1,comb,t)

            return
        dfs(n-1,[],target)
        return ans

        
