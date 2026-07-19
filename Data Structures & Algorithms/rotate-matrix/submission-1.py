class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for r in range(n//2):
            matrix[r], matrix[n-r-1] = matrix[n-r-1], matrix[r]

        for r in range(n):
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]