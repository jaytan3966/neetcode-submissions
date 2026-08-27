class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pairs = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        n = len(digits)
        ans = []

        if digits == "": return ans

        def dfs(i, cur):
            if len(cur) == n:
                ans.append(cur)
                return
            lets = pairs[digits[i]]

            for let in lets:
                dfs(i+1, cur+let)
            return
        dfs(0, "")
        return ans