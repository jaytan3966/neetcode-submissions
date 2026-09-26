# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0, 0
            
            take_left, skip_left = dfs(root.left)
            take_right, skip_right = dfs(root.right)

            take_this = root.val + skip_left + skip_right
            skip_this = max(take_left, skip_left) + max(skip_right, take_right)

            return take_this, skip_this
        
        take_this, skip_this = dfs(root)
        return max(take_this, skip_this)