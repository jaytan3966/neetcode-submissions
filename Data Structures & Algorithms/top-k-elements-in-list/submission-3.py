class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = []

        for i in range(n):
            buckets.append([])
        cnts = Counter(nums)
        for num in cnts:
            buckets[cnts[num]-1].append(num)

        ans = []
        while k>0:
            lastBucket = buckets.pop()
            while k>0 and lastBucket:
                ans.append(lastBucket.pop())
                k-=1
        return ans