# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def bfs(root):
            nonlocal ans

            queue = []
            count = 0
            if root:
                queue.append(root)
                count = 1
            while queue:
                for i in range(count):
                    node = queue.pop(0)
                    if i == count-1:
                        ans.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                count = len(queue)
        bfs(root)
        return ans