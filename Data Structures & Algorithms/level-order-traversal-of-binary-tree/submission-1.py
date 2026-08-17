# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        def bfs(root):
            nonlocal ans

            queue = deque()
            count = 0
            if root:
                queue.append(root)
                count = 1

            while queue:
                row = []
                for _ in range(count):
                    node = queue.popleft()
                    row.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                count = len(queue)
                ans.append(row)
        bfs(root)
        return ans
                
                    