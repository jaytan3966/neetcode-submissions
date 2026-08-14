class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        counts = Counter(nums)

        for num in counts:
            buckets[counts[num]-1].append(num)
        
        ans = []
        for i in range(len(buckets)-1, -1, -1):
            if len(ans) == k:
                return ans
            curBucket = buckets[i]
            j = len(curBucket)-1
            while j>-1 and len(ans) != k:
                ans.append(curBucket[j])
                j-=1
        return ans