class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i : [] for i in range(n)}
        
        for l,r in edges:
            if l>r:
                l,r = r, l
            graph[l].append(r)
        
        q = deque([0])
        visited = set()
        while q:
            cur = q.popleft()
            for nei in graph[cur]:
                if nei in visited: return False
                q.append(nei)
                visited.add(nei)
            visited.add(cur)
        return True