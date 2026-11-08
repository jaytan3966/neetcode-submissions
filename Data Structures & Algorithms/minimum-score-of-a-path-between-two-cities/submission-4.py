from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        neighbors = defaultdict(list)

        for a,b, dist in roads:
            neighbors[a].append((dist, b))
            neighbors[b].append((dist, a))

        stack = neighbors[1]

        ans = float('inf')
        visited = set()
        visited.add(1)

        while stack:
            dist, nei = stack.pop()

            visited.add(nei)
            if dist<ans:
                ans = dist

            for d, n in neighbors[nei]:
                if n not in visited:
                    stack.append((d, n))
        return ans