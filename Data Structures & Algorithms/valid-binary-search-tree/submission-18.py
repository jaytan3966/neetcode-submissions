# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        if root.left:
            if root.left.val >= root.val: return False
        if root.right:
            if root.right.val <= root.val: return False
        
        left = self.isValidBST(root.left)
        right = self.isValidBST(root.right)

        return left and right