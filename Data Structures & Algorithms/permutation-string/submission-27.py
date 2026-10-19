class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if n>m:
            return False
        
        counts = {}
        for r in range(n):
            counts[s1[r]] = counts.get(s1[r],0)+1

        l = 0
        found = {}
        for r in range(m):
            found[s2[r]] = found.get(s2[r],0)+1

            if r-l+1 > n:
                found[s2[l]]-=1

                if found[s2[l]]==0:
                    del found[s2[l]]
                l+=1

            if counts == found:
                return True
        return False