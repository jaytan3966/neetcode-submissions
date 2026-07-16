# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        small = float('-inf')
        great = float('inf')
        def dfs(root, smallest, greatest):
            if not root:
                return True
            if root.val > greatest or root.val < smallest:
                return False
            left = dfs(root.left, smallest, root.val)
            right = dfs(root.right, root.val, greatest)
            
            return left and right
        return dfs(root, small, great)
