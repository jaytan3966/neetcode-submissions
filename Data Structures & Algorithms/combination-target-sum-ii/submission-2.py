class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        n = len(candidates)

        ans = []

        def dfs(i, cur, total):
            if total == target:
                ans.append(cur[:])
                return
            if i>=n or total > target:
                return

            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            cur.pop()

            while i+1<n and candidates[i] == candidates[i+1]:
                i+=1

            dfs(i+1, cur, total)

            return
        
        dfs(0, [], 0)
        return ans