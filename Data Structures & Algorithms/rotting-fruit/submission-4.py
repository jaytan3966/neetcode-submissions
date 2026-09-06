class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        fresh = rotting = 0
        q = deque([])
        visited = set()

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    rotting+=1
                    q.append((r,c))
                    visited.add((r,c))
        if not fresh: return 0
        if fresh and not rotting: return -1

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        count = -1

        while q:
            l = len(q)
            for _ in range(l):
                r,c = q.popleft()

                for y,x in dirs:
                    if (0<=r+y<n and 0<=c+x<m) and (r+y, c+x) not in visited:
                        if grid[r+y][c+x] == 1:
                            grid[r+y][c+x]=2
                            fresh-=1
                            q.append((r+y, c+x))
            count+=1
        
        return -1 if fresh else count

        