# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(root):
            nonlocal ans
            if not root: return 0
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            if ans:
                ans = abs(right-left)<=1
            return max(left, right)
        dfs(root)
        return ans