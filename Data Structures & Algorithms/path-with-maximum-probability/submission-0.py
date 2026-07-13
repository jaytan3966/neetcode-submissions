class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, edge in enumerate(edges):
            v, nei = edge[0], edge[1]

            graph[v].append((succProb[i], nei))
            graph[nei].append((succProb[i], v))

        mh = [(-1, start_node)]
        visited = set()
        visited.add(start_node)

        while mh:
            p, cur = heapq.heappop(mh)
            visited.add(cur)

            if cur == end_node: return -p

            for prob, nei in graph[cur]:
                if nei not in visited:
                    heapq.heappush(mh, ((p*prob), nei))
        return 0.0