class Solution:
    def numSquares(self, n: int) -> int:
        squares = []

        i = 1
        while i*i <= n:
            squares.append(i*i)
            i+=1
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(1,n+1):

            for square in squares:
                if square<=i:
                    dp[i] = min(1+dp[i-square], dp[i])
                else:
                    break
        
        return dp[n]