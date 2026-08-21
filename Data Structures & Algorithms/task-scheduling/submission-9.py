class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        time = 0
        h = []
        q = deque([])

        for l in counts:
            heapq.heappush(h, (-counts[l],l))
        
        while h or q:
            time+=1
            if h:
                c, l = heapq.heappop(h)
                c+=1
                if c!=0: #next available time
                    nxt = time+n
                    q.append((nxt, c, l))
            if q and q[0][0]<=time:
                nxt, c, l = q.popleft()
                heapq.heappush(h, (c,l))

        return time

        
