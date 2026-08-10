class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        n = len(candidates)
        
        def dfs(i, comb, cur):
            if cur == target:
                ans.append(comb[:])
                return
            if cur>target or i>=n:
                return
            
            comb.append(candidates[i])
            dfs(i+1, comb, cur+candidates[i])
            comb.pop()

            while i+1<n and candidates[i] == candidates[i+1]: i+=1
            dfs(i+1, comb, cur)

        dfs(0, [], 0)
        return ans
            
