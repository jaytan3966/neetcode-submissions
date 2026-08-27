class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        
        maps = {"2":"abc","3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv","9":"wxyz"}
        n = len(digits)
        ans = []

        def dfs(cur, i):
            if i == n:
                ans.append(cur)
                return
            num = digits[i]
            chars = maps[num]

            for char in chars:
                dfs(cur+char, i+1)
            
        dfs("", 0)
        return ans