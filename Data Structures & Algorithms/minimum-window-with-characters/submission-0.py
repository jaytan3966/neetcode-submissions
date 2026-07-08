class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        n, m = len(s), len(t)
        if n<m or s == "" or t == "": return ans
        if s == t: return s

        ans = [-1,-1]
        counts = {}
        for i in range(m):
            counts[t[i]] = counts.get(t[i],0)+1
        
        cur = {}
        have, need = 0, len(counts)
        l = 0
        ansLen = float('inf')
        for r in range(n):
            c = s[r]

            if counts.get(c,0):
                cur[c] = cur.get(c,0)+1
            if c in counts and cur[c] == counts[c]:
                have+=1
            
            while have == need:
                if r-l+1 < ansLen:
                    ansLen = r-l+1
                    ans = l, r
                if s[l] in counts: cur[s[l]]-=1
                if s[l] in counts and cur[s[l]]<counts[s[l]]: have-=1
                l+=1
        l, r = ans
        return s[l:r+1] if l != -1 else ""
        
                

