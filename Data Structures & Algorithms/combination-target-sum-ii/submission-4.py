class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        n = len(candidates)

        def dfs(i, total, comb):
            if total == target:
                ans.append(comb[:])
                return
            
            if i >= n:
                return
            
            if total>target:
                return
            
            comb.append(candidates[i])
            dfs(i+1, total+candidates[i], comb)
            comb.pop()

            while i+1<n and candidates[i]==candidates[i+1]:
                i+=1
            
            dfs(i+1, total, comb)

            return
        
        dfs(0, 0, [])
        return ans