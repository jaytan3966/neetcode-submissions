class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counts = Counter(s1)
        l = 0

        for r in range(len(s2)):
            print(counts)
            if s2[r] in counts and counts[s2[r]] != 0: 
                counts[s2[r]]-=1
                if all(x == 0 for x in counts.values()): return True
            else:
                if s2[l] in counts: counts[s2]+=1
                l+=1
            
        return False
        

