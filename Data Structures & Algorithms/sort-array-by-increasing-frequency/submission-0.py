class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mh = []
        counts = Counter(nums)

        for num in counts:
            heapq.heappush(mh, (counts[num], -num))
        
        ans = []
        while mh:
            count, num = heapq.heappop(mh)

            for i in range(count):
                ans.append(-num)
        return ans

