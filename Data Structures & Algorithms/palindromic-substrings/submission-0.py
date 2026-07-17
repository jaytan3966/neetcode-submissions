class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        def expand(l,r):
            nonlocal ans
            while 0<=l<=r<n and s[l] == s[r]:
                ans+=1
                l-=1
                r+=1
            return
        
        for i in range(n):
            expand(i,i)
            expand(i,i+1)
        return ans