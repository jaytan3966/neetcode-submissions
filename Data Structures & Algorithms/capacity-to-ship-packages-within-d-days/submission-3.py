class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
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

            if bins <= days: 
                r = mid-1
            else:
                l = mid+1

        return l