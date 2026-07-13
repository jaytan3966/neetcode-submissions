class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = min(piles), sum(piles)
        n = len(piles)

        ans = float('inf')
        while l<=r:
            mid = (l+r)//2

            hours = 0
            i = 0
            for i in range(n):
                hours+=(piles[i]+mid-1) // mid

            if hours <= h:
                ans = min(ans, mid)
                r = mid-1
            else:
                l = mid+1
        return ans