class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])

        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0 or matrix[r][c] == float("-inf"):
                    if matrix[0][c] == 1 or matrix[0][c] == float("inf"): 
                        matrix[0][c] = float("inf")
                    else: 
                        matrix[0][c] = float("-inf")

                    if matrix[r][0] == 1 or matrix[r][0] == float("inf"):
                        matrix[r][0] = float("inf")
                    else:
                        matrix[r][0] = float("-inf")

        for r in range(n):
            if matrix[r][0] == float("inf") or matrix[r][0] == float("-inf"):
                for c in range(m):
                    matrix[r][c] = 0
        
        for c in range(m):
            if matrix[0][c] == float("inf") or matrix[0][c] == float("-inf"):
                for r in range(n):
                    matrix[r][c] = 0

        