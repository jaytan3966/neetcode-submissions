class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        
        if n>m: return False

        target = [0]*26
        cur = [0]*26

        for i in range(n):
            target[ord(s1[i])-ord('a')]+=1
            cur[ord(s2[i])-ord('a')]+=1
        
        l=0
        for r in range(n,m+1):
            if target==cur: return True

            if r<m:
                cur[ord(s2[l])-ord('a')]-=1
                l+=1
                cur[ord(s2[r])-ord('a')]+=1
        return False
        
        