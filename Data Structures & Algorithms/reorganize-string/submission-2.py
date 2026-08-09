class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = []
        n = len(s)
        counts = Counter(s)
        ans = ""

        for ch in counts:
            if counts[ch]*2>(n+1): return ans

            heapq.heappush(maxHeap, (-counts[ch], ch))
        
        coolDown = None

        while maxHeap:
            count, ch = heapq.heappop(maxHeap)

            if coolDown:
                heapq.heappush(maxHeap, coolDown)
                coolDown = None

            ans+=ch

            if count+1 == 0: continue

            coolDown = (count+1, ch)
        
        return ans