class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        time = 0
        h = []
        q = deque([])

        for l in counts:
            heapq.heappush(h, -counts[l])
        
        while h or q:
            time+=1
            if h:
                c = heapq.heappop(h)
                c+=1
                if c!=0: #next available time
                    nxt = time+n
                    q.append((nxt, c))
            if q and q[0][0]<=time:
                nxt, c = q.popleft()
                heapq.heappush(h, c)

        return time

        
