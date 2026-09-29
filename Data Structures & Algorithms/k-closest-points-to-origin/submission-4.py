class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_h = []

        for x,y in points:
            heapq.heappush(max_h, (-((x**2 + y**2) ** 0.5), [x,y]))

            if len(max_h)>k:
                heapq.heappop(max_h)
        
        ans = []
        for item in max_h:
            ans.append(item[1])
        
        return ans