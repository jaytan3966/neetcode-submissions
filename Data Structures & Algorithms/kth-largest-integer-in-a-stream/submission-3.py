class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = [n for n in nums]

        heapq.heapify(self.minHeap)
        self.k = k

        while len(self.minHeap)>k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:

        if len(self.minHeap) == self.k: heapq.heappushpop(self.minHeap, val)
        else: heapq.heappush(self.minHeap, val)
        return self.minHeap[0]