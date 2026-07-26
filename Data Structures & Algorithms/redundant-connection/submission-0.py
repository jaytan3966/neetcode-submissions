class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = {i+1 : [] for i in range(n)}

        for p,c in edges:
            graph[p].append(c)
        
        visited = set()
        for p,c in edges:
            if c in visited: return [p,c]

            visited.add(c)
        

