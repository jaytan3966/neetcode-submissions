class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lR, rR = 0, len(matrix)-1
        mR = 0
        while lR<=rR:
            mR = (lR+rR)//2
            if matrix[mR][0]>target:
                rR = mR-1
            elif matrix[mR][-1]<target:
                lR = mR+1
            else:
                break
        lC, rC = 0, len(matrix[mR])-1
        while lC<=rC:
            mC = (lC+rC)//2
            if matrix[mR][mC]>target:
                rC = mC-1
            elif matrix[mR][mC]<target:
                lC = mC+1
            else:
                return True
        return False
