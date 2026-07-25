# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mh = []
        
        while head:
            heapq.heappush(mh, head.val)
            head = head.next
        
        newHead = ListNode()
        dummy = newHead

        while mh:
            newNode = ListNode(heapq.heappop(mh))
            dummy.next = newNode
            dummy = dummy.next
        
        return newHead.next