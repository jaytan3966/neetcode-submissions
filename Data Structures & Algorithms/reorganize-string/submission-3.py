class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = Counter(s)
        maxHeap = [(-counts[ch], ch) for ch in counts]
        heapq.heapify(maxHeap)

        ans = ""

        for ch in counts:
            if counts[ch]*2>(n+1): return ans
        
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