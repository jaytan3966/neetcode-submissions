# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        
        def dfs(root, greatest):
            nonlocal cnt
            if root.val>=greatest:
                cnt+=1
            greatest = max(greatest, root.val)
            if root.left:
                dfs(root.left, greatest)
            if root.right:
                dfs(root.right, greatest)
        if root:
            dfs(root, float('-inf'))
        return cnt
