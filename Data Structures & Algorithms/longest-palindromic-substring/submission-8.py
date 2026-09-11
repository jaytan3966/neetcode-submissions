class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        ans = s[0]
        greatest = 1
        for i in range(n-1):
            l, r = i-1, i+1
            curLen = 1

            while 0<=l<r<n and s[l]==s[r]:
                curLen+=2
                l-=1
                r+=1
            
            if curLen>greatest:
                greatest = curLen
                ans = s[l+1:r]
            
            if s[i] == s[i+1]:
                l, r = i, i+1
                curLen = 0

                while 0<=l<r<n and s[l]==s[r]:
                    curLen+=2
                    l-=1
                    r+=1
            
                if curLen>greatest:
                    greatest = curLen
                    ans = s[l+1:r]
        
        return ans