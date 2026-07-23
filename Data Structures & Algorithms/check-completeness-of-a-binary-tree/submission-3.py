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
            hole = False
            anotherLevel = False

            for i in range(n):
                cur = q.popleft()

                if not cur and anotherLevel: return False

                if hole and cur: return False

                if i<n and not cur: 
                    hole = True

                if cur:
                    q.append(cur.left)
                    q.append(cur.right)

                    if cur.left or cur.right:
                        anotherLevel = True
        return True