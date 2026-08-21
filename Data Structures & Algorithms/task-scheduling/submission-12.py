class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        remaining = deque([])

        counts = Counter(tasks)
        for task in counts:
            heapq.heappush(maxHeap, (-counts[task], task))
        
        time = 0
        while maxHeap or remaining:
            if remaining:
                if remaining[0][0] == time:
                    time, rem, task = remaining.popleft()
                    heapq.heappush(maxHeap, (rem, task))
            if maxHeap:
                rem, task = heapq.heappop(maxHeap)
                if rem != -1: remaining.append((time+n+1, rem+1, task))
            time+=1
        return time