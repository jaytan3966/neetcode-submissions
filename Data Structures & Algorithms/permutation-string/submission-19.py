class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n>m: return False

        targ = [0]*26
        ans = [0]*26
        for i in range(n):
            targ[ord(s1[i])-ord('a')]+=1
            ans[ord(s2[i])-ord('a')]+=1

        if targ==ans: return True
        
        l = 0
        for r in range(n, m):
            ans[ord(s2[l])-ord('a')]-=1
            l+=1
            ans[ord(s2[r])-ord('a')]+=1
            if targ==ans: return True
        return targ==ans
            

        