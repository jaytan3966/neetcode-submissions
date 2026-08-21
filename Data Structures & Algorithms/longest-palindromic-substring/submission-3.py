class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = s[0]
        cnt = 1

        for i in range(n):
            l,r = i-1,i+1

            while 0<=l<r<n and s[l]==s[r]:
                l-=1
                r+=1
            newCnt = r-l-1
            if newCnt > cnt:
                ans = s[l+1:r]
            
            si = i+1
            if si<n and s[i]==s[si]:
                l,r = i-1, si+1
                while 0<=l<r<n and s[l]==s[r]:
                    l-=1
                    r+=1
                newCnt = r-l-1
                if newCnt > cnt:
                    ans = s[l+1:r]
        return ans
