# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_tree = float('-inf')
        def dfs(root):
            if not root: return 0

            nonlocal max_tree

            left = dfs(root.left)
            right = dfs(root.right)

            max_tree = max(max_tree,left+root.val+right, root.val)
            return max(left+root.val, right+root.val, root.val)

        dfs(root)
        return max_tree