class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        out_degrees = defaultdict(int)

        for x,y in edges:
            out_degrees[x]+=1
            out_degrees[y]+=1
        
        cands = []
        for node in out_degrees:
            if out_degrees[node] != 1:
                cands.append(node)

        if not cands:
            cands = [0]
        return cands