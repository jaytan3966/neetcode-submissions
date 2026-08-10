class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cur = num[:3]
        ans = float('-inf')
        l = 0
        n = len(num)

        for r in range(3, n+1):
            if int(cur)%111 == 0:
                ans = max(ans, int(cur))
            if r == n: break
            l+=1
            cur = num[l:r+1]

        if ans == 0: return '000'

        return str(ans) if ans != float('-inf') else ""
