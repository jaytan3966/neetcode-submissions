class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        aCheap = []
        bCheap = []

        for i, cost in enumerate(costs):
            a,b = cost

            heapq.heappush(aCheap, (a-b,i))
            heapq.heappush(bCheap, (b-a,i))

        ans = 0
        n = len(costs)//2
        seen = set()
        for i in range(n):
            a, l = heapq.heappop(aCheap)
            b, r = heapq.heappop(bCheap)

            while l in seen:
                a,l = heapq.heappop(aCheap)
            while r in seen:
                b,r = heapq.heappop(bCheap)

            ans+=costs[l][0]
            ans+=costs[r][1]
        return ans

    
