# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        newHead = None
        tail = slow
        while tail:
            nxt = tail.next
            tail.next = newHead
            newHead = tail
            tail = nxt
        
        ans = 0
        while head and newHead:
            if head.val+newHead.val>ans: ans = head.val+newHead.val
            head = head.next
            newHead = newHead.next
        return ans
