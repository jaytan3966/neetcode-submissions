"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}

        dummy = head
        cur = Node(0)
        dum = cur
        while dummy:
            nodes[dummy] = Node(dummy.val)
            dum.next = nodes[dummy]
            dum = dum.next
            dummy = dummy.next
        
        dummy = head
        while dummy:
            if dummy.random: nodes[dummy].random = nodes[dummy.random]
            dummy = dummy.next
        
        return cur.next
