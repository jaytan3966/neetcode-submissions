class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)

        def dfs(i, chars):
            if i == n:
                return len(chars)
            
            skip = dfs(i+1, chars)

            new_chars = chars
            for j in range(len(arr[i])):
                if arr[i][j] in chars:
                    new_chars = None
                    break
                else:
                    new_chars.add(arr[i][j])

            take = 0
            if new_chars is not None:
                take = dfs(i+1, new_chars)
            
            return max(skip, take)
        
        chars = set()
        return dfs(0, chars)
                
