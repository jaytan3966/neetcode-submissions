# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root: return (0,0)

            left, grandLeft = dfs(root.left)
            right, grandRight = dfs(root.right)

            cur = root.val+grandLeft+grandRight
            skipRoot = (max(left,grandLeft) + max(right,grandRight))
            return (cur, skipRoot)
        return max(dfs(root))

