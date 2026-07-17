# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        cnt = k
        def dfs(root):
            nonlocal ans, cnt
            if not root:
                return
            dfs(root.left)
            cnt-=1
            if cnt == 0:
                ans = root.val
                return
            dfs(root.right)
        dfs(root)
        return ans