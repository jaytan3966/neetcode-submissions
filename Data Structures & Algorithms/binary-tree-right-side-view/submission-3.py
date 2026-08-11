# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = [root.val]
        queue = deque()

        queue.append(root)
        cnt = 1

        while queue:
            
            for _ in range(cnt):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if queue:
                ans.append(queue[-1].val)
            cnt = len(queue)
            
        return ans