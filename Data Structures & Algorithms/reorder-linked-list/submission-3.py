# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def reverse(root):
            prev = None
            while root:
                nxt = root.next
                root.next = prev
                prev = root
                root = nxt
            return prev
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        newHead = slow.next
        slow.next = None
        newHead = reverse(newHead)

        dummy = head
        while newHead:
            tmp1 = dummy.next
            tmp2 = newHead.next

            dummy.next = newHead
            newHead.next = tmp1

            dummy = tmp1
            newHead = tmp2