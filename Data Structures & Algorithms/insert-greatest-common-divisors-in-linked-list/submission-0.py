# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        newNode = ListNode()
        while dummy and dummy.next:
            newNode = ListNode(math.gcd(dummy.val, dummy.next.val))
            nxt = dummy.next
            dummy.next = newNode
            newNode.next = nxt
            dummy = nxt
        newNode.next = dummy
        return head