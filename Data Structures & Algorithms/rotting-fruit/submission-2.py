class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        seen = set()
        fresh = 0
        n, m = len(grid), len(grid[0])

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    q.append((r,c))
                    seen.add((r,c))
                if grid[r][c] == 1:
                    fresh+=1
        if len(q) == 0:
            if not fresh: return 0
            if fresh: return -1


        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        ans = -1

        while q:
            l = len(q)
            for _ in range(l):
                r,c = q.popleft()
                grid[r][c] = 2
                for y,x in dirs:
                    if 0<=r+y<n and 0<=c+x<m and grid[r+y][c+x] == 1 and (r+y,c+x) not in seen:
                        q.append((r+y,c+x))
                        seen.add((r+y, c+x))
                        fresh-=1
            ans+=1
        return ans if fresh == 0 else -1
