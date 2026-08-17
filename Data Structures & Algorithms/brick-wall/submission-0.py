class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        
        counts = {}
        for r in range(n):
            cur = 0
            for c in range(len(wall[r])):
                if c > 0:
                    cur+=wall[r][c-1]
                    counts[cur] = counts.get(cur,0)+1
        return n-max(counts.values(), default=0)
