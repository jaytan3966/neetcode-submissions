class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        ans = []
        def dfs(i, comb, total):
            if total == target:
                ans.append(comb[:])
                return
            
            if i==n or total>target:
                return
            
            comb.append(candidates[i])
            total+=candidates[i]
            dfs(i+1, comb, total)

            comb.pop()
            total-=candidates[i]
            while i+1<n and candidates[i] == candidates[i+1]:
                i+=1

            dfs(i+1, comb, total)

            return
        dfs(0, [], 0)
        return ans
            