class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counts = Counter(nums)

        buckets = [[] for _ in range(n+1)]
        for num in counts:
            buckets[counts[num]].append(num)

        ans = []
        for b in range(n, -1, -1):
            k-=len(buckets[b])
            for num in buckets[b]: ans.append(num)
            if k == 0: break
        return ans

