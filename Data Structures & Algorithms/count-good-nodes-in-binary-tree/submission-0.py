# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        cnt = 0

        def dfs(root, greatest):
            nonlocal cnt
            print(root.val, greatest)
            if root.left:
                if root.left.val >= greatest:
                    cnt +=1
                dfs(root.left, max(greatest, root.left.val))
            if root.right:
                if root.right.val >= greatest:
                    cnt +=1
                dfs(root.right, max(greatest, root.right.val))
        if root:
            cnt+=1
            dfs(root, root.val)
        return cnt
