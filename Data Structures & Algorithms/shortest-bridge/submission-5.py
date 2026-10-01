class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque([])

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    q.append((r,c))
                    break
            if q:
                break
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        cur_island = set()

        starting_island = deque([])
        while q:
            r, c = q.popleft()

            if (r,c) in cur_island: continue

            cur_island.add((r,c))
            starting_island.append((0,r,c))
            
            for y,x in dirs:
                if 0<=r+y<n and 0<=c+x<m and (r+y,c+x) not in cur_island and grid[r+y][c+x] == 1:
                    q.append((r+y,c+x))

        visited = cur_island  
        while starting_island:
            dist, r, c = starting_island.popleft()

            for y, x in dirs:
                nr, nc = r + y, c + x

                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:

                    if grid[nr][nc] == 1:
                        return dist

                    visited.add((nr, nc))
                    starting_island.append((dist + 1, nr, nc))
        

