class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        a,b = 0,0

        dp = {}

        def dfs(l,r):
            if l>r: return 0
            if (l,r) in dp: return dp[(l,r)]

            even = (r-l)%2 == 1
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            dp[(l,r)] = max(left + dfs(l+1,r), right + dfs(l,r-1))
            return dp[(l,r)]

        total = sum(piles)
        alice = dfs(0,len(piles)-1)
        return alice>(total-alice)