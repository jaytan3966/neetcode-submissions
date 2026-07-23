class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        n = len(s)
        farthest = 0

        if s[n-1] != '0': return False

        while q:
            ind = q.popleft()
            start = max(ind+minJump, farthest+1)
            for i in range(start, min(ind+maxJump+1, n)):
                if s[i] == '0': 
                    q.append(i)
                    if i == n-1: return True
            farthest = ind + maxJump
        return False