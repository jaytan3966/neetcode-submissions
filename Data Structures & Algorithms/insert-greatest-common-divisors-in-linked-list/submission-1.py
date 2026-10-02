# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = head

        while dummy:
            if dummy.next:
                nxt = dummy.next
                dummy.next = ListNode(math.gcd(dummy.val, dummy.next.val), nxt)
                dummy = nxt
            else:
                dummy = dummy.next
        return head
