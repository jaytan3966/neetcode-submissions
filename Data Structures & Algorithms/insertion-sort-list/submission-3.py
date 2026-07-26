# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()

        minHeap = []
        while head:
            heapq.heappush(minHeap, head.val)
            head = head.next
        
        dummy = newHead
        while minHeap:
            cur = heapq.heappop(minHeap)
            dummy.next = ListNode(cur)
            dummy = dummy.next
        return newHead.next