class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i, pair in enumerate(edges):
            s, nei = pair[0], pair[1]
            graph[s].append((nei, succProb[i]))
            graph[nei].append((s, succProb[i]))
        
        best = [0.0]*n
        best[start_node] = 1
        maxHeap = [(-1.0, start_node)]

        while maxHeap:
            prob, cur = heapq.heappop(maxHeap)

            prob = -prob

            if cur == end_node: return prob
            for nei, p in graph[cur]:
                new_prob = prob*p

                if new_prob>best[nei]:
                    best[nei] = new_prob
                    heapq.heappush(maxHeap, (-new_prob, nei))
        return 0.0



        