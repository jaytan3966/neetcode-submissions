# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode()
        dummy = newNode

        rem = 0
        while l1 or l2 or rem:
            l = l1.val if l1 else 0
            r = l2.val if l2 else 0

            tot = (l+r+rem)%10
            rem = (l+r+rem)//10

            node = ListNode(tot)
            dummy.next = node
            dummy = dummy.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return newNode.next


