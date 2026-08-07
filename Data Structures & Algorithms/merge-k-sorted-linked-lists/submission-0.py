# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1, l2):
            if not l1: return l2
            if not l2: return l1

            if l1.val<l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2
        
        n = len(lists)
        if n == 0 or n == 1: return lists[0] if n == 1 else None

        new = []
        for i in range(0, n, 2):
            newList = merge(lists[i], lists[i+1] if i<n-1 else None)
            new.append(newList)
        return self.mergeKLists(new)
        