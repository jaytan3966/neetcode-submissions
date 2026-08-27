class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {"2":"abc","3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv","9":"wxyz"}
        n = len(digits)
        ans = []

        def dfs(cur, i):
            if i == n:
                ans.append(cur)
                return

            for char in maps[digits[i]]:
                dfs(cur+char, i+1)
        
        if digits: dfs("", 0)
        return ans