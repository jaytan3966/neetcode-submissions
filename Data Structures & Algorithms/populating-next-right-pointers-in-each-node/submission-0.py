"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([root])

        while q:
            n = len(q)
            prev = q.popleft()
            
            if prev.left:
                q.append(prev.left)
                q.append(prev.right)

            for i in range(1, n):
                cur = q.popleft()
                prev.next = cur
                prev = cur
                if cur.left:
                    q.append(cur.left)
                    q.append(cur.right)

        return root
                