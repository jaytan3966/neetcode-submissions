# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None

        def merge_list(root1, root2):
            new_head = ListNode()
            dummy = new_head

            while root1 and root2:
                new_node = None

                if root1.val<root2.val:
                    new_node = ListNode(root1.val)
                    root1 = root1.next
                else:
                    new_node = ListNode(root2.val)
                    root2 = root2.next
                
                dummy.next = new_node
                dummy = dummy.next
            
            if root1: dummy.next = root1
            if root2: dummy.next = root2

            return new_head.next
        
        while len(lists)>1:
            list1 = lists.pop()
            list2 = lists.pop()

            new_list = merge_list(list1, list2)

            lists.append(new_list)
        
        return lists[0]
