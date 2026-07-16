# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        dummy = ans
        carry = 0
        while l1 and l2:
            ans.val = (l1.val + l2.val + carry)%10
            carry = int((l1.val + l2.val + carry)/10)
            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                ans.next = ListNode()
                ans = ans.next
        while l1:
            ans.val = (l1.val+carry)%10
            carry = int((l1.val + carry)/10)
            l1 = l1.next
            if l1:
                ans.next = ListNode()
                ans = ans.next
        while l2:
            ans.val = (l2.val+carry)%10
            carry = int((l2.val + carry)/10)
            l2 = l2.next
            if l2:
                ans.next = ListNode()
                ans = ans.next
        if carry>0:
            ans.next = ListNode(1)
        return dummy
