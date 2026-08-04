class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice, bob = 0, 0
        l,r = 0, len(piles)-1
        turn = 1

        while l<=r:
            amnt = 0
            if piles[l]>=piles[r]:
                amnt = piles[l]
                l+=1
            else:
                amnt = piles[r]
                r-=1
            if turn%2: alice+=amnt
            else: bob+=amnt
            turn+=1
        return alice>bob
