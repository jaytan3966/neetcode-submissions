class Solution:
    def coloredCells(self, n: int) -> int:
        count = 1

        for i in range(2,n+1):
            count+=(4*(i-1))
        
        return count
