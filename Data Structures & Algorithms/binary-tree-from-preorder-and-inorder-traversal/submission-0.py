# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ino = {val: idx for idx, val in enumerate(inorder)}
        n = len(preorder)

        ind = 0
        def dfs(l,r):
            if l > r: return None

            nonlocal ind

            nodeVal = preorder[ind]
            ind+=1

            mid = ino[nodeVal]
            node = TreeNode(nodeVal)
            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)

            return node
        return dfs(0, n-1)





