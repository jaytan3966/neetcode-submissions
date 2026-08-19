"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def regionSum(startR, startC, endR, endC):
            ans = 0
            for r in range(startR, endR):
                for c in range(startC, endC):
                    ans+=grid[r][c]
            return ans
            
        n = len(grid)
        m = len(grid[0])

        head = Node()
        dummy = head

        q = deque([(dummy, 0, 0, n, m)])

        while q:
            cur, startR, startC, r, c = q.popleft()
            tot = regionSum(startR, startC, r, c)

            if tot == (r-startR)*(c-startC) or tot == 0:
                cur.val = tot!=0
                cur.isLeaf = 1
            else:
                newR = startR+(r-startR)//2
                newC = startC+(c-startC)//2

                topLeft = Node()
                topRight = Node()
                botLeft = Node()
                botRight = Node()

                cur.topLeft = topLeft
                cur.topRight = topRight
                cur.bottomLeft = botLeft
                cur.bottomRight = botRight

                q.append((topLeft, startR, startC, newR, newC))
                q.append((topRight, startR, newC, newR, c))
                q.append((botLeft, newR, startC, r, newC))
                q.append((botRight, newR, newC, r, c))

                cur.isLeaf = 0
                cur.val = 0
        return head




