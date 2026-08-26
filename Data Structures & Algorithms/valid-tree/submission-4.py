class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i : [] for i in range(n)}
        
        for l,r in edges:
            graph[l].append(r)
            graph[r].append(l)
        
        q = deque([(0,-1)])
        visited = set()
        visited.add(0)

        while q:
            cur, par = q.popleft()
            for nei in graph[cur]:
                if nei == par: continue
                if nei in visited: return False
                q.append((nei, cur))
                visited.add(nei)
        return len(visited) == n