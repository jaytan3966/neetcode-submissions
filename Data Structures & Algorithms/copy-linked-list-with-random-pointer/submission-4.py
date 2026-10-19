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

        if not head:
            return None
            
        new_nodes = {}

        dummy = head

        while dummy:
            new_node = Node(dummy.val)
            new_nodes[dummy] = new_node
            dummy = dummy.next
        
        dummy = head
        while dummy:
            new_node = new_nodes[dummy]
            
            next_node = new_nodes.get(dummy.next, None)
            new_node.next = next_node
            random_node = new_nodes.get(dummy.random, None)
            new_node.random = random_node

            dummy = dummy.next
        
        return new_nodes[head]
