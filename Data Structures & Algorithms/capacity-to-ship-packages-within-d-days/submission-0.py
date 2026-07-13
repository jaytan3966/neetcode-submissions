class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        weights.sort()
        l, r = weights[-1], sum(weights)
        n = len(weights)

        if n == days: return l

        while l<=r:
            mid = (l+r)//2

            curTot = 0
            bins = 1
            for i in range(n):
                if curTot+weights[i]<=mid:
                    curTot+=weights[i]
                else:
                    curTot = weights[i]
                    bins+=1
            print(mid, bins)
            if bins == days: return mid
            if bins>days:
                l = mid+1
            else:
                r = mid-1
        return l