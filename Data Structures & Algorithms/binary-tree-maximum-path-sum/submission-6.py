# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, cur_sum):
            if not root: return cur_sum

            if root.val<0:
                cur_sum = 0

            left = dfs(root.left, cur_sum)
            right = dfs(root.right, cur_sum)

            if root.val<0:
                return max(left, right)
            else:
                return left+root.val+right

        return dfs(root, 0) 