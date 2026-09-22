class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        ans = []

        for i, val in enumerate(nums):
            while q and q[-1][1]<val:
                q.pop()
            
            q.append((i, val))
            while q and q[0][0]+k<=i:
                q.popleft()
            
            if i>=k-1:
                ans.append(q[0][1])
        return ans

