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

        ans = self.sameTree(root, subRoot)

        if not ans:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)

            return left or right
        return ans
    def sameTree(self, root, subRoot):
        if not root and not subRoot: return True

        if not (root and subRoot): return False

        if root.val != subRoot.val: return False

        l = self.sameTree(root.left, subRoot.left)
        r = self.sameTree(root.right, subRoot.right)

        return l and r