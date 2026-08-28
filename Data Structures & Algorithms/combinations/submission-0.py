class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(i, comb):
            if len(comb) == k:
                ans.append(comb[:])
                return
            for num in range(i, n+1):
                comb.append(num)
                dfs(num+1, comb)
                comb.pop()
            return
        dfs(1, [])
        return ans