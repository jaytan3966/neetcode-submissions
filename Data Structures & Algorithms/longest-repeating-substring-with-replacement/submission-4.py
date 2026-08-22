class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        table = {s[i]: 0 for i in range(len(s))}
        maxFreq = 0
        res = 0

        while r<len(s):
            print(l, r, res, maxFreq)
            table[s[r]]+=1
            if table[s[r]]>maxFreq: maxFreq = table[s[r]]

            if (r-l+1) - maxFreq <= k:
                res = max(res, r-l+1)
                r+=1
            else: 
                if maxFreq == table[s[l]]: maxFreq-=1
                table[s[l]]-=1
                l+=1
                
        return res

            