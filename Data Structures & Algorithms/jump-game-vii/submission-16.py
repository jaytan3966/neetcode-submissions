class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        seen = set()
        seen.add(0)
        n = len(s)

        while q:
            ind = q.popleft()

            if ind == n-1:
                return True

            start = ind+minJump
            for i in range(start, min(ind+maxJump+1, n)):
                if s[i] == '0':
                    q.append(i)
                    seen.add(i)
        
        return False