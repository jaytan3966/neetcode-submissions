class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        neg = x<0

        x = abs(x)

        while x:
            i = x%10
            ans*=10
            ans+=i

            x = int(x/10)
        
        if not (-2 **31 <= ans <= 2**31-1): return 0

        return ans if not neg else -ans