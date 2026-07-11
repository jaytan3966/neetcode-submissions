# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root, cur):
            nonlocal ans

            cur = (cur*10)+root.val

            if not (root.left or root.right): 
                ans+=cur
                return

            if root.left: dfs(root.left, cur)

            if root.right: dfs(root.right, cur)

            return

        dfs(root, 0)
        return ans