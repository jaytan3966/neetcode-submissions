class MedianFinder:

    def __init__(self):
        self.left = [] #max heap
        self.right = [] #min heap

    def addNum(self, num: int) -> None:
        if self.right and self.right[0]<=num:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
            
        if len(self.right)>len(self.left)+1:
            num = heapq.heappop(self.right)
            heapq.heappush(self.left, -num)
        if len(self.left)>len(self.right)+1:
            num = heapq.heappop(self.left)
            heapq.heappush(self.right, -num)

    def findMedian(self) -> float:
        n = len(self.left)
        m = len(self.right)
        size = n+m

        if self.left and size % 2 == 0:
            return (-self.left[0] + self.right[0])/2
        return self.right[0] if m>n else -self.left[0]
