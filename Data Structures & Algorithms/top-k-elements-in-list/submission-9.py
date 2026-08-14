class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucks = [[] for _ in range(n)]
        counts = Counter(nums)
        
        for num in counts:
            bucks[counts[num]-1].append(num)
        
        ans = []
        for i in range(n-1, -1, -1):
            if k == 0: return ans
            for num in bucks[i]:
                ans.append(num)
                k-=1
        return ans