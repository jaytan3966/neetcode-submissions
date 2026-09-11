# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)

        if not root:
            return newNode

        def dfs(root):
            if not root: return

            if val<root.val:
                if root.left:
                    dfs(root.left)
                else:
                    root.left = newNode
                    return
            else:
                if root.right:
                    dfs(root.right)
                else:
                    root.right = newNode
                    return
        dfs(root)

        return root
