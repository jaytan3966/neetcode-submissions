class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pairs = {}
        minHeap = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            pairs[dist] = point
            
            heapq.heappush(minHeap, (dist, point))
        
        ans = []
        
        while len(ans)!=k:
            dist, point = heapq.heappop(minHeap)
            ans.append(point)
            
        return ans
