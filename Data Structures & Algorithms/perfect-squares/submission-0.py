class Solution:
    def numSquares(self, n: int) -> int:
        squares = []

        i = 1
        while i*i <= n:
            squares.append(i*i)
            i+=1
        
        dp = [0] * (n+1)
        dp[1] = 1

        for i in range(2, n+1):
            minimum = float('inf')
            for square in squares:
                if square<=i:
                    minimum = min(minimum, dp[i-square])
                else:
                    break
            dp[i] = 1 + minimum
            
        return dp[n]