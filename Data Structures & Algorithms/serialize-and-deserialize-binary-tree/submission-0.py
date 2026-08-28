# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []
        queue = deque()

        if root: queue.append(root)
        else: return ""

        while queue:
            node = queue.popleft()
            if not node: data.append('N')
            else:
                data.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return '#'.join(data)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        data = data.split('#')
        if data[0] == 'N' or data[0] == "": return None

        root = TreeNode(int(data[0]))
        queue = deque([root])
        i = 1
        
        while queue:
            node = queue.popleft()
            if data[i] != 'N':
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            i+=1
            if data[i] != 'N':
                node.right = TreeNode(int(data[i]))
                queue.append(node.right)
            i+=1

        return root