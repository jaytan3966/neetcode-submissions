# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return not root and not subRoot
        
        ans = False
        if root.val == subRoot.val:
            left = self.isSubtree(root.left, subRoot.left)
            right = self.isSubtree(root.right, subRoot.right)
            ans = left and right
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            ans = left or right
        return ans
        