# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True

        if not (root and subRoot): return False

        if root.val == subRoot.val:
            l = self.isSubtree(root.left, subRoot.left)
            r = self.isSubtree(root.right, subRoot.right)

            return l and r
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)

        return l or r