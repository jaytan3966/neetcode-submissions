"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        oldToNew = {}

        oldToNew[node] = Node(node.val)
        q = deque([])
        q.append(node)

        while q:
            cur = q.popleft()
            neighs = cur.neighbors

            for n in neighs:
                if n not in oldToNew:
                    newNode = Node(n.val)
                    oldToNew[n] = newNode
                    oldToNew[cur].neighbors.append(newNode)
                    q.append(n)
                else:
                    oldToNew[cur].neighbors.append(oldToNew[n])
        return oldToNew[node]
