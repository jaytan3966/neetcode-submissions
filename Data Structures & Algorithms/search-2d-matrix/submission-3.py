class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row, r_row = 0,len(matrix)-1

        while l_row<=r_row:
            mid_row = (l_row+r_row)//2

            l, r = 0, len(matrix[mid_row])-1

            if matrix[mid_row][l]<=target<=matrix[mid_row][r]:
                while l<=r:
                    mid = (l+r)//2
                    if matrix[mid_row][mid] == target:
                        return True
                    elif matrix[mid_row][mid] > target:
                        r = mid-1
                    else:
                        l = mid+1
                return False
            elif matrix[mid_row][l] > target:
                r_row = mid_row-1
            else:
                l_row = mid_row+1
        return False