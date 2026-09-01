# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        ans = 0
        def dfs(root, greatest):
            nonlocal ans
            if root.val>=greatest:
                ans+=1
            newG = root.val if root.val>=greatest else greatest

            if root.left: dfs(root.left, newG)
            if root.right: dfs(root.right, newG)
        dfs(root, root.val)
        return ans