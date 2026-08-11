class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]

        rows = len(board)
        cols = len(board[0])
        n = len(word)
        seen = set()

        def dfs(i, r,c):
            found = False

            if i >= n:
                return True
            if not 0<=r<rows or not 0<=c<cols or board[r][c] != word[i]:
                return False

            seen.add((r,c))
            for y, x in dirs:
                if (r+y, c+x) not in seen:
                    found = dfs(i+1, r+y, c+x)
                    if found:
                        return True
            seen.remove((r,c))
            return False
        
        for r in range(rows):
            for c in range(cols):
                found = dfs(0,r,c)
                if found: return True
        return False
        
                