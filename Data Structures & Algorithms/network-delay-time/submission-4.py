class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connections = {}

        for src, target, time in times:
            if src not in connections:
                connections[src] = []
            connections[src].append((time, target))
        
        min_h = [(0, k)]
        heapq.heapify(min_h)

        ans = 0
        visited = set()

        while min_h:
            time, src = heapq.heappop(min_h)

            if src in visited: 
                continue

            ans = time
            visited.add(src)

            if len(visited) == n:
                break
                
            for edge_time, target in connections.get(src, []):
                if target not in visited:
                    heapq.heappush(min_h, (time+edge_time, target))

        return ans if len(visited) == n else -1


