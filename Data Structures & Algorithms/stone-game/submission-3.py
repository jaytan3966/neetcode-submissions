class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        def dfs(l,r):
            if l>r: return 0
            if dp[l][r] != -1: return dp[l][r]

            turn = (r-l)%2 == 0
            left = piles[l] if turn else 0
            right = piles[r] if turn else 0

            return max(dfs(l+1,r)+left, dfs(l,r-1)+right)
        
        total = sum(piles)
        return dfs(0,n-1)>(total//2)


