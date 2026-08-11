class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        q = deque([(n-1, n-1)])
        count = 0
        dirs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

        visited = set()

        while q:
            m = len(q)
            for _ in range(m):
                r,c = q.popleft()
                if (r,c) == (0,0) and grid[r][c] == 0: return count+1
                visited.add((r,c))

                for y,x in dirs:
                    if 0<=r+y<n and 0<=c+x<n and (r+y,x+c) not in visited and grid[r+y][x+c]==0:
                        q.append((r+y,x+c))
            count+=1
        return -1