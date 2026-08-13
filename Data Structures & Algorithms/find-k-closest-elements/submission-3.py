class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        q = deque([])
        cop = k
        diffs = [(abs(arr[i]-x), arr[i]) for i in range(n)]

        for i in range(n):
            if q and q[0][0]>diffs[i][0]:
                if k == 0:
                    q.popleft()
            if k != 0: k-=1
            q.append(diffs[i])
        return [q[i][1] for i in range(cop)]

