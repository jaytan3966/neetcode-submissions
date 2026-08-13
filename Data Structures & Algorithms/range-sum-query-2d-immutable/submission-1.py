class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.pref = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for r in range(n):
            for c in range(m):
                self.pref[r+1][c+1] = matrix[r][c] + self.pref[r][c+1] + self.pref[r+1][c] - self.pref[r][c] 


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pref[row2+1][col2+1] - self.pref[row1][col2+1] - self.pref[row2+1][col1] + self.pref[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)