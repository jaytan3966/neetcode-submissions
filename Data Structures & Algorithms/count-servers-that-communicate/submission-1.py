class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        rows = [0]*n
        cols = [0]*m
        seen = set()

        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    rows[r]+=1
                    cols[c]+=1
                    seen.add((r,c))
        ans = 0
        for r, c in seen:
            if rows[r]>1 or cols[c]>1: ans+=1
        return ans
