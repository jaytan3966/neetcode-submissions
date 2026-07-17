# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        ans = 0
        def dfs(root, k):
            nonlocal ans, cnt
            if not root:
                return
            left = dfs(root.left, k)
            cnt+=1
            if cnt == k:
                ans = root.val
            right = dfs(root.right, k)
            
        dfs(root, k)
        return ans