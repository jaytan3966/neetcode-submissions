class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        table = {s[i]: 0 for i in range(len(s))}
        maxFreq, res = 0, 0

        while r<len(s):

            table[s[r]]+=1
            maxFreq = max(maxFreq, table[s[r]])

            while (r-l+1) - maxFreq > k:
                table[s[l]]-=1
                l+=1
            res = max(res, (r-l+1))
            r+=1
                
        return res

            