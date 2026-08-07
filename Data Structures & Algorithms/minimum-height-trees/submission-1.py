class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n <= 2:
            return list(range(n))

        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        leaves = deque(i for i in range(n) if len(adj[i]) == 1)
        remaining = n

        while remaining > 2:
            remaining -= len(leaves)
            next_leaves = deque()
            for leaf in leaves:
                neighbor = adj[leaf].pop()  
                adj[neighbor].discard(leaf)
                if len(adj[neighbor]) == 1:
                    next_leaves.append(neighbor)
            leaves = next_leaves

        return list(leaves)

