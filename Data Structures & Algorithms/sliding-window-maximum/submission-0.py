class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maxHeap = []
        ans = []
        for i in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))

            while maxHeap[0][1] <= i-k:
                heapq.heappop(maxHeap)
            if i>=k-1:
                ans.append(-maxHeap[0][0])
        return ans