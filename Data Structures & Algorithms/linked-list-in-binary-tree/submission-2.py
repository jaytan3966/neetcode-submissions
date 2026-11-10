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
        
        stack = [root]
        while stack:
            node = stack.pop()

            if match(node, head):
                return True
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False