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
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        second = reverse(second)
        while second:
            nxt1, nxt2 = head.next, second.next
            head.next = second
            second.next = nxt1
            head = nxt1
            second = nxt2
