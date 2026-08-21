class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = len(tasks)
        counts = Counter(tasks)

        maxHeap = [(-counts[task], task) for task in set(tasks)]
        heapq.heapify(maxHeap)
        waiting = deque([])

        ans = 0
        i = 0
        while i<l:
            if maxHeap:
                count, task = heapq.heappop(maxHeap)
                count+=1

                if count != 0:
                    waiting.append(((count, task), ans+n))
                i+=1

            if waiting and waiting[0][1]<=ans:
                task, ind = waiting.popleft()
                heapq.heappush(maxHeap, task)
                
            ans+=1
            print(f'heap: {maxHeap} {ans} {i}')
            print(f'waiting: {waiting}')

        return ans