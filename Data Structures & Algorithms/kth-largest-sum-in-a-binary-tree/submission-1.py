# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])

        min_h = []
        while q:
            size = len(q)

            cur_sum = 0

            for _ in range(size):
                cur_node = q.popleft()
                cur_sum+=cur_node.val

                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
        
            heapq.heappush(min_h, cur_sum)

            if len(min_h)>k:
                heapq.heappop(min_h)
        
        if len(min_h) < k:
            return -1
        return min_h[0]