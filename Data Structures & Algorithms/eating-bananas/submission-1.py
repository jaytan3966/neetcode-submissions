class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = float('inf')

        while l<=r:
            mid = (l+r)//2

            hrs = 0
            for num in piles:
                hrs+=math.ceil(num/mid)
            if hrs > h:
                l = mid+1
            else:
                ans = min(ans, mid)
                r = mid-1
        return ans