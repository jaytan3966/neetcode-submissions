# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_array = []

        dummy = head
        while dummy:
            reversed_array.append(dummy.val)
            dummy = dummy.next
        reversed_array.reverse()

        n = len(reversed_array)
        new_array = []
        greatest = float('-inf')

        for i in range(n):
            if reversed_array[i]<greatest:
                continue
            greatest = max(greatest, reversed_array[i])
            new_array.append(reversed_array[i])

        new_head = ListNode()
        dummy = new_head
        for i in range(len(new_array)-1, -1, -1):
            new_node = ListNode(new_array[i])
            dummy.next = new_node
            dummy = dummy.next
        return new_head.next