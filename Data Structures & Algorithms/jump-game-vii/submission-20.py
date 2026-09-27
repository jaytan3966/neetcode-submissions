class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        n = len(s)

        while q:
            start = q.popleft()

            for i in range(minJump, maxJump+1):
                if s[start] == '0':
                    if start+i == n-1:
                        return True
                    q.append(start+i)
        return False
