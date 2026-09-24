class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])

        seen_rows = set()
        ans = 0
        for r in range(n):
            if sum(grid[r]) > 1:
                seen_rows.add(r)
                ans+=sum(grid[r])
        
        for c in range(m):
            total = 0
            new_server = 0
            for r in range(n):
                total+=grid[r][c]

                if r not in seen_rows and grid[r][c]:
                    new_server+=1
            if total>1:
                ans+=new_server
        return ans
