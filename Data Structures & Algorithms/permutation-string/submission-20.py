class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1), len(s2)

        if n>m: return False

        counts = [0]*26
        for i in range(n):
            counts[ord(s1[i])-ord('a')]+=1
        
        counts2 = [0]*26
        for i in range(n):
            counts2[ord(s2[i])-ord('a')]+=1
        
        l = 0
        for r in range(n,m):
            if counts == counts2: return True
            counts2[ord(s2[l])-ord('a')]-=1
            counts2[ord(s2[r])-ord('a')]+=1
            l+=1
        return counts == counts2