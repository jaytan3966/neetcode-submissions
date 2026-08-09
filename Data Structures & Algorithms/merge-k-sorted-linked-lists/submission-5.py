# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1, l2):
            head = ListNode()
            dummy = head

            while l1 and l2:
                if l1.val<l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            if l1: dummy.next = l1
            if l2: dummy.next = l2
            return head.next
        
        n = len(lists)
        if n == 0: return None

        while len(lists) != 1:
            new = []
            n = len(lists)
            for i in range(0, n, 2):
                newList = lists[i]
                if i<n-1:
                    newList = merge(lists[i], lists[i+1])
                new.append(newList)
            lists = new
        return lists[0]
        