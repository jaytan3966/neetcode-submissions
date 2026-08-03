class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        seen = set()
        components = 0

        for l,r in edges:
            graph[l].append(r)
            graph[r].append(l)
        
        def dfs(c):
            if c in seen: return
            seen.add(c)

            for nei in graph[c]:
                if nei not in seen: dfs(nei)
            return
        for i in range(n):
            if i not in seen:
                components+=1
                dfs(i)
        return components