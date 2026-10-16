# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cnt = 0

        dummy = head
        while dummy:
            cnt+=1
            dummy = dummy.next
        
        ans = []
        per_seg = cnt//k
        extra = cnt%k
        dummy = head

        for i in range(k):
            list_length = per_seg

            if i<extra:
                list_length+=1

            new_head = dummy
            
            for j in range(list_length-1):
                dummy = dummy.next
            
            if dummy:
                nxt = dummy.next
                dummy.next = None
                dummy = nxt
            
            ans.append(new_head)
        return ans



        
