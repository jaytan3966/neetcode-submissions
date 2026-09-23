class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])

        ans = []
        n = len(nums)

        for i in range(n):
            while q and q[-1][0]<nums[i]:
                q.pop()
            q.append((nums[i], i))

            while q and q[0][1]<=i-k:
                q.popleft()

            if i>=k-1:
                ans.append(q[0][0])
        return ans