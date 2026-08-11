# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        pVal = p.val
        qVal = q.val
        ans = None
        def dfs(root):
            nonlocal pVal
            nonlocal qVal
            nonlocal ans
            if ans:
                return
            if pVal<=root.val and root.val<=qVal or qVal<=root.val and root.val<=pVal:
                ans = root
                return
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)
        return ans
            