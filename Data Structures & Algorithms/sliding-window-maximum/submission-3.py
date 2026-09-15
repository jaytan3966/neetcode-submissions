class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        n = len(nums)

        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i], i))
        
        ans = [-maxHeap[0][0]]

        for i in range(k, n):
            while maxHeap and maxHeap[0][1]<=i-k:
                heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-nums[i], i))
            ans.append(-maxHeap[0][0])
        return ans
