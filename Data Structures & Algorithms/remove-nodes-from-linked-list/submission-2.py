# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        dummy = head
        while dummy:
            cur = dummy.val
            while stack and cur>stack[-1]:
                stack.pop()
            stack.append(cur)
            dummy = dummy.next
        
        new_head = ListNode()
        dummy = new_head
        for num in stack:
            new_node = ListNode(num)
            dummy.next = new_node
            dummy = dummy.next
        return new_head.next