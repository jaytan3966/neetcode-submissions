class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap)>1:
            greatest = -heapq.heappop(maxHeap)
            sec = -heapq.heappop(maxHeap)

            if greatest == sec: continue
            else:
                greatest-=sec
                heapq.heappush(maxHeap, -greatest)
        return 0 if not maxHeap else -heapq.heappop(maxHeap)