# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        smallest = float('-inf')
        biggest = float('inf')
        def dfs(root, smallest, biggest):
            if not root:
                return True
            if root.val >= biggest or root.val<=smallest:
                return False
            return dfs(root.left, smallest, root.val) and dfs(root.right, root.val, biggest)
        return dfs(root, smallest, biggest)
        
                