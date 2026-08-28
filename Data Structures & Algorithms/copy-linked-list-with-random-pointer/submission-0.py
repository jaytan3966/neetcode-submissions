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
        oldToNew = {}
        dummy = head

        while dummy:
            newNode = Node(dummy.val)
            oldToNew[dummy] = newNode
            dummy = dummy.next
        
        dummy = head
        newNode = oldToNew[dummy]
        ans = newNode
        while dummy:
            newNode.next = oldToNew.get(dummy.next, None)
            newNode.random = oldToNew.get(dummy.random, None)
            newNode = newNode.next
            dummy = dummy.next
        return ans






