class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([])
        n = len(s)
        seen = set()

        if s[n-1] != '0': return False
        q.append(0)
        seen.add(0)

        while q:
            ind = q.popleft()

            for i in range(minJump, maxJump+1):
                if i+ind in seen: continue
                if ind+i >= n: continue
                if s[ind+i] != '0': continue
                if ind+i == n-1: return True

                q.append(ind+i)
                seen.add(ind+i)
        return False