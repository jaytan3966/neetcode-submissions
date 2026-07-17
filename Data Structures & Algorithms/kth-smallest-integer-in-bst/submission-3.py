# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        cnt = 0
        targ = k
        def dfs(root):
            nonlocal ans, cnt, targ
            if not root:
                return
            dfs(root.left)
            cnt+=1
            if cnt == targ:
                ans = root.val
                return
            dfs(root.right)
        dfs(root)
        return ans