class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        q = deque([])
        seen = {}

        for r in range(n):
            if grid[r][0] == 1:
                q.append((r,0))
                seen[(r,0)] = True
            if grid[r][m-1] == 1:
                q.append((r,m-1))
                seen[(r,m-1)] = True
        
        for c in range(1, m-1):
            if grid[0][c] == 1:
                q.append((0,c))
                seen[(0,c)] = True
            if grid[n-1][c] == 1:
                q.append((n-1, c))
                seen[(n-1,c)] = True
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            r,c = q.popleft()

            for y,x in dirs:
                if 0<=r+y<n and 0<=c+x<m:
                    if (r+y, c+x) not in seen and grid[r+y][c+x] == 1:
                        q.append((r+y, c+x))
                        seen[(r+y, c+x)] = True
        
        ones = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    ones+=1
        return ones-len(seen)


