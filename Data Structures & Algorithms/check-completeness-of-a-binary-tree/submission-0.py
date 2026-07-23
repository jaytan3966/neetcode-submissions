# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])

        while q:
            n = len(q)
            for i in range(n):
                cur = q.popleft()

                if not cur.left and i<n-1: return False

                q.append(cur.left)
                if not cur.right:
                    if i == n-1: return True
                q.append(cur.right)
        return True