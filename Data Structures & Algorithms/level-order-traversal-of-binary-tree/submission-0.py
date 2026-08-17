# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        ans = []
        queue = deque()
        
        queue.append(root)
        cnt = len(queue)

        while queue:
            level = []
            for _ in range(cnt):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            cnt = len(queue)
            if len(level)>0:
                ans.append(level)
        return ans


