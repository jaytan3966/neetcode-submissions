from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        #map city to smallest distance
        smallest_dist = {}

        #map city to all reachable cities
        reachable = defaultdict(set)
        for a,b, dist in roads:
            smallest_dist[a] = min(smallest_dist.get(a, float('inf')), smallest_dist.get(b, float('inf')), dist)
            smallest_dist[b] = min(smallest_dist.get(b, float('inf')), smallest_dist.get(a, float('inf')), dist)
            
            reachable[a].add(b)
            reachable[b].add(a)
        
        ans = float('inf')
        for city in reachable[n]:
            ans = min(ans, smallest_dist[city])
        return ans