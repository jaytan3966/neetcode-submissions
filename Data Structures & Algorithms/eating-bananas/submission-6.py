class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, sum(piles)
        n = len(piles)
        ans = float('inf')
        while l<=r:
            mid = (l+r)//2

            time = 0
            for i in range(n):
                time+=math.ceil(piles[i]/mid)
            if time<=h:
                ans = min(mid, ans)
                r = mid-1
            else:
                l = mid+1
        return ans