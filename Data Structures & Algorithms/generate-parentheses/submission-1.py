class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(cur, l, r):
            if l+r == n*2:
                ans.append(cur)
                return
            if l<n: dfs(cur+'(', l+1, r)
            if r<l: dfs(cur+')', l, r+1)
        dfs("", 0,0)
        return ans