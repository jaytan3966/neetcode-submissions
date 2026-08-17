# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)

        ans = []
        while queue:
            n = len(queue)
            row = []
            for i in range(n):
                cur = queue.popleft()
                if cur:
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                    row.append(cur.val)
            if len(row) > 0:
                ans.append(row)
        return ans

            