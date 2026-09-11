# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head: return None
        
        dummy = head
        n = 0

        while dummy:
            if dummy.next:
                tail = dummy.next
            dummy = dummy.next
            n+=1
        
        k %= n

        if k == 0: return head

        k = n-k

        prevTail = None
        newHead = head
        while k>0:
            newHead = newHead.next

            if not prevTail:
                prevTail = head
            else:
                prevTail = prevTail.next
            k-=1
        prevTail.next = None
        tail.next = head

        return newHead
        


