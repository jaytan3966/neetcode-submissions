class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        minHeap = []

        for i in range(len(names)):
            pair = (-heights[i], names[i])
            heapq.heappush(minHeap, pair)

        ans = []
        while minHeap:
            height, name = heapq.heappop(minHeap)
            ans.append(name)
        return ans