# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_head = slow.next
        slow.next = None

        prev = None
        while second_head:
            nxt = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = nxt
        second_head = prev

        dummy = head
        while second_head:
            tmp1 = dummy.next
            tmp2 = second_head.next

            dummy.next = second_head
            second_head.next = tmp1

            dummy = tmp1
            second_head = tmp2