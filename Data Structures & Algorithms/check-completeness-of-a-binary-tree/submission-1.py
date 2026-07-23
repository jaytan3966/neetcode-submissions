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
            for i in range(n):
                cur = q.popleft()
                if hole and cur: return False
                if i<n and cur==None: 
                    hole = True
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)
        return True