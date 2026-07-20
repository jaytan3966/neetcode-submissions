class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counts = Counter(s1)
        l, r = 0, 0

        while r<len(s2):
            print(counts,l, r) 
            if s2[r] in counts and counts[s2[r]] != 0: 
                counts[s2[r]]-=1
                if all(x == 0 for x in counts.values()): return True
                r+=1
            else:
                if s2[l] in counts: counts[s2[l]]+=1
                l+=1
                r=l

            
        return False
        

