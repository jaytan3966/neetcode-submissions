# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        queue = deque()
        count = 0
        if root: 
            queue.append(root)
            count = 1

        while queue:
            n = len(queue)
            row = []
            for i in range(n):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

                if i == n-1:
                    ans.append(node.val)
        return ans
