# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            return prev

        def getKth(head, k):
            while head and k>1:
                head = head.next
                k-=1
            if not head: return None
            return head
        
        def goToEnd(head):
            while head.next:
                head = head.next
            return head

        ans = ListNode()
        dummy = ans
        cur = head
        fast = head

        while fast:
            fast = getKth(fast, k)
            if not fast:
                break
            nxt = fast.next
            fast.next = None
            dummy.next = reverse(cur)
            dummy = goToEnd(dummy)
            fast = nxt
            cur = fast
        if cur:
            dummy = goToEnd(dummy)
            dummy.next = cur
        return ans.next

        