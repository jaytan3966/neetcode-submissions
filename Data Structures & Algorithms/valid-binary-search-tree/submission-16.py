# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        valid = True
        def dfs(root, smallest, biggest):
            nonlocal valid
            if not root or not valid:
                return valid
            if root.left:
                if root.left.val>=biggest:
                    valid = False
                dfs(root.left, smallest, root.val)
            if root.right:
                if root.right.val<=smallest:
                    valid = False
                dfs(root.right, root.val, biggest)
        dfs(root, root.val, root.val)
        return valid
                