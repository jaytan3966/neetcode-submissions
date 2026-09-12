class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = max(piles)

        while l<r:
            mid = (l+r)//2

            hours = 0
            for pile in piles:
                hours+=math.ceil(pile/mid)

            if hours<=h:
                ans = min(ans, mid)
                r = mid
            else:
                l = mid+1
        return ans
