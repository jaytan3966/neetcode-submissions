# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def reverse(head):
            prev = None
            dummy = head

            while dummy:
                nxt = dummy.next
                dummy.next = prev
                prev = dummy
                dummy = nxt
            return prev
        
        dummy = head
        while dummy:
            dummy.next = reverse(dummy.next)
            dummy = dummy.next
