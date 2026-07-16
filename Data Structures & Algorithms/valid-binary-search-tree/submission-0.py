# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, smallest, greatest):
            
            left = True
            right = True
            if root.left:
                if root.left.val>smallest:
                    return False
                left = dfs(root.left, min(smallest, root.left.val), max(greatest, root.left.val))
            if root.right:
                if root.right.val<greatest:
                    return False
                left = dfs(root.right, min(smallest, root.right.val), max(greatest, root.right.val))
        
            return left and right
        if root:
            return dfs(root, root.val, root.val)
        return True
        