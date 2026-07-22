class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l<=r:
            mRow = (l+r)//2
            f, s = 0, len(matrix[0])-1
            if matrix[mRow][f] <= target <= matrix[mRow][s]:
                while f<=s:
                    mid = (f+s)//2
                    if matrix[mRow][mid] == target:
                        return True
                    elif matrix[mRow][mid]>target:
                        s = mid-1
                    else:
                        f = mid+1
                return False
            elif matrix[mRow][f]>target:
                r = mRow-1
            else:
                l = mRow+1
        return False