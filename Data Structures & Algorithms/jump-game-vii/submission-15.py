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

            for i in range(minJump, maxJump+1):
                if ind+i<n and ind+i not in seen and s[ind+i] == '0':
                    q.append(ind+i)
                    seen.add(ind+i)
        
        return False