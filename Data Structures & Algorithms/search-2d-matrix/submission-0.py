class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lR, rR = 0, len(matrix)-1
        while lR<=rR:
            mR = (lR+rR)//2
            lC, rC = 0, len(matrix[mR])-1
            while lC<=rC:
                mC = (lC+rC)//2
                if matrix[mR][lC]>target:
                    rR = mR-1
                    break
                elif matrix[mR][rC]<target:
                    lR = mR+1
                    break
                else:
                    if matrix[mR][mC]>target:
                        rC = mC-1
                    elif matrix[mR][mC]<target:
                        lC = mC+1
                    else:
                        return True
        return False
