class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        seen = set()

        n, m = len(grid), len(grid[0])
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    q.append((r,c))
                    seen.add((r,c))

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        dist = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = min(grid[i][j], dist)
                for y, x in dirs:
                    if 0<=i+y<n and 0<=j+x<m and grid[i+y][j+x] != -1 and (i+y,j+x) not in seen:
                        seen.add((i+y, j+x))
                        q.append((i+y,j+x))
            dist+=1


