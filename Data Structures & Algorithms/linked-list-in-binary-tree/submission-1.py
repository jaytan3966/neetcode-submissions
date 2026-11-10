class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def match(root, head):
            if not head:
                return True

            if not root:
                return False

            if root.val != head.val:
                return False

            return (match(root.left, head.next) or
                    match(root.right, head.next))
        
        if not head:
            return True
        
        if not root:
            return False

        return match(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)