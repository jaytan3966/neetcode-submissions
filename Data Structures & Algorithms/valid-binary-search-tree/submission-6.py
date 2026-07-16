# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        valid = True
        def dfs(root):
            nonlocal valid
            if not root or not valid:
                return valid
            if root.left:
                if root.left.val>=root.val:
                    valid = False
                self.isValidBST(root.left)
            if root.right:
                if root.right.val<=root.val:
                    valid = False
                self.isValidBST(root.right)
        dfs(root)
        return valid
                