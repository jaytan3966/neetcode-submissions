class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        ans = 0
        heights = [0]*m

        for r in matrix:
            for c in range(m):
                if r[c] == 1:
                    heights[c]+=1
                else:
                    heights[c]=0
            sorted_heights = sorted(heights, reverse=True)

            for c, height in enumerate(sorted_heights):
                width = c+1
                ans = max(ans, width*height)
        return ans