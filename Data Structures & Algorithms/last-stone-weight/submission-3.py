class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        while len(maxHeap)!=1:
            top = -heapq.heappop(maxHeap)
            sec = -heapq.heappop(maxHeap)

            if top == sec: heapq.heappush(maxHeap, 0)
            if top < sec: heapq.heappush(maxHeap, -(sec-top))
            if top > sec: heapq.heappush(maxHeap, -(top-sec))
        return -heapq.heappop(maxHeap)