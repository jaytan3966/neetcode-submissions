class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        a, b = 0, 0

        def expand(l,r):
            while 0<=l<=r<n and s[l] == s[r]:
                l-=1
                r+=1
            return [l,r]

        for i in range(n):
            l, r = expand(i,i)
            if r-l-2 > b-a:
                a,b = l+1, r-1

            l,r = expand(i, i+1)
            if r-l-2 > b-a:
                a,b = l+1, r-1

        return s[a:b+1]
