# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        ans = 0
        def dfs(root, great):
            nonlocal ans

            if root.val>=great: ans+=1

            if root.left: dfs(root.left, max(great, root.val))
            if root.right: dfs(root.right, max(great, root.val))

            return
        dfs(root, 0)

        return ans