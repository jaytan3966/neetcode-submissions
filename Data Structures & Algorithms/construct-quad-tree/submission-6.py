"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def totalGrid(startR, startC, endR, endC):
            ans = grid[startR][startC]

            for r in range(startR, endR):
                for c in range(startC, endC):
                    if grid[r][c] != ans: return False
            return True
        n,m = len(grid), len(grid[0])
        
        q = deque([])
        head = Node()
        q.append((head, 0, 0, n, m))

        while q:
            cur, startR, startC, endR, endC = q.popleft()
            same = totalGrid(startR, startC, endR, endC)

            if same:
                cur.val = grid[startR][startC]
                cur.isLeaf = 1
            else:
                midR = (startR+endR)//2
                midC = (startC+endC)//2
                cur.topLeft = Node()
                cur.topRight = Node()
                cur.bottomLeft = Node()
                cur.bottomRight = Node()

                q.append((cur.topLeft, startR, startC, midR, midC))
                q.append((cur.topRight, startR, midC, midR, endC))
                q.append((cur.bottomLeft, midR, startC, endR, midC))
                q.append((cur.bottomRight, midR, midC, endR, endC))

                cur.val = 0
                cur.isLeaf = 0
        return head

            
