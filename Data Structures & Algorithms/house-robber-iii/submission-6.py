# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        memo = {}

        def dfs(root, skip):
            if not root:
                return 0

            if (root, skip) in memo:
                return memo[(root, skip)]

            not_rob = dfs(root.left, False) + dfs(root.right, False)
            memo[(root, skip)] = not_rob
            if skip:
                return not_rob
            
            rob = root.val + dfs(root.left, True) + dfs(root.right, True)
            memo[(root, skip)] = max(rob, not_rob)
            return max(rob, not_rob)

        return max(dfs(root, False), dfs(root, True))

