class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        for x,y in points:
            dist = math.sqrt((x**2)+(y**2))
            heapq.heappush(minHeap, (dist, [x,y]))
        
        ans = []
        while minHeap and k>0:
            dist, pair = heapq.heappop(minHeap)
            ans.append(pair)
            k-=1
        return ans