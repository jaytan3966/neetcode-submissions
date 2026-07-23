class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([])
        n = len(s)

        if s[n-1] != '0': return False
        q.append(0)

        while q:
            m = len(q)
            for _ in range(m):
                ind = q.popleft()

                for i in range(minJump, maxJump+1):
                    if ind+i >= n: continue
                    if s[ind+i] != '0': continue
                    if ind+i == n-1: return True

                    q.append(ind+i)
        return False