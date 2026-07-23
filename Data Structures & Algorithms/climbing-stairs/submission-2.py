class Solution:
    def climbStairs(self, n: int) -> int:

        sec, first = 1, 1
        
        for i in range(n):
            temp = first
            first = sec + first
            sec = temp
        return sec

