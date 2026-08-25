class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def dfs(comb, l, r):
            if len(comb) == n*2:
                ans.append(comb[:])
                return
            if l<n:
                dfs(comb+'(', l+1, r)
            if r<l:
                dfs(comb+')', l, r+1)

        dfs("", 0,0)
        return ans