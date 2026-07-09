# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def getKth(head, k):
            while head and k>1:
                head = head.next
                k-=1
            if not head: return None
            return head

        prevGroup = ListNode()
        nextGroup = None
        ans = prevGroup
        cur = head

        while True:
            h = cur
            tail = getKth(cur, k)
            if not tail: break

            nextGroup = tail.next
            tail.next = None

            prev = None
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            prevGroup.next = prev
            prevGroup = h
            cur = nextGroup

        if nextGroup:
            prevGroup.next = nextGroup
        return ans.next

        