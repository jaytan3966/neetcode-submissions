# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None: return None
        
        n = 0
        dummy = head
        while dummy:
            n+=1
            dummy = dummy.next
        
        k%=n

        if k == 0: return head

        newHead = None
        dummy = head

        while dummy:
            nxt = dummy.next
            dummy.next = newHead
            newHead = dummy
            dummy = nxt

        dummy = newHead
        while k>1:
            dummy = dummy.next
            k-=1
        
        secondHalf = dummy.next
        dummy.next = None

        #reverse first half
        prev = None
        while newHead:
            nxt = newHead.next
            newHead.next = prev
            prev = newHead
            newHead = nxt
        newHead = prev

        #reverse second half
        prev = None
        while secondHalf:
            nxt = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = nxt
        secondHalf = prev

        dummy = newHead
        while dummy and dummy.next:
            dummy = dummy.next
        dummy.next = secondHalf

        return newHead

