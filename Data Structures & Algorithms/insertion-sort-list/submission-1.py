# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        dummy = newHead

        minHeap = []
        while head:
            heapq.heappush(minHeap, head.val)
            head = head.next
        
        while minHeap:
            val = heapq.heappop(minHeap)
            newNode = ListNode(val)

            dummy.next = newNode
            dummy = dummy.next
        return newHead.next