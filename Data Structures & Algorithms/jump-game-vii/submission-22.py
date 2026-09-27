class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        n = len(s)
        farthest = 0

        while q:
            start = q.popleft()
            start = max(start, farthest)
            for i in range(minJump, maxJump+1):
                if start+i<n and s[start+i] == '0':
                    if start+i == n-1:
                        return True
                    q.append(start+i)
                    farthest = max(farthest, start+i)
        return False
