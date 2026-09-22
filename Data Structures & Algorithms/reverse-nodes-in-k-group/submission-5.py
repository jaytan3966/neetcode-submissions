# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def find_kth(root, k):

            kth = root
            while k>1 and kth:
                kth = kth.next
                k-=1
            return kth
        
        def reverse(root):
            new_head = None
            new_tail = root
            while root:
                nxt = root.next
                root.next = new_head
                new_head = root
                root = nxt
            
            return new_head, new_tail

        dummy = head
        final_head = None
        prev_tail = None

        while dummy:
            kth = find_kth(dummy, k)
            
            if not kth:
                if prev_tail:
                    prev_tail.next = dummy
                break

            next_head = kth.next
            kth.next = None

            new_head, new_tail = reverse(dummy)
            if not final_head:
                final_head = new_head
            
            if prev_tail:
                prev_tail.next = new_head

            new_tail.next = next_head
            prev_tail = new_tail
            dummy = next_head

        return final_head