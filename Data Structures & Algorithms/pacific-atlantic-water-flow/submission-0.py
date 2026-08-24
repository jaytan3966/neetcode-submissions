class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        pacific = set()
        atlantic = set()

        n = len(heights)
        m = len(heights[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c, origin, water):
            if not (0<=r<n and 0<=c<m):
                return
            if (r,c) in water or heights[r][c] < origin: return

            water.add((r,c))

            for y,x in dirs:
                dfs(r+y,c+x,heights[r][c],water)
            return
        
        for r in range(n):
            dfs(r,0,heights[r][0], pacific)
            dfs(r,m-1,heights[r][m-1], atlantic)
        for c in range(m):
            dfs(0,c,heights[0][c], pacific)
            dfs(n-1,c,heights[n-1][c], atlantic)

        return [[r,c] for r,c in atlantic if (r,c) in pacific]

        