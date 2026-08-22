class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        count1, count2 = 1,0
        res = 0

        while r<len(s):
            print(l, r, res)
            if s[r] != s[l]: count2+=1
            else: count1+=1

            if (r-l+1) - max(count1, count2) <= k:
                res = max(res, r-l+1)
                r+=1
            else: 
                l+=1
                r=l+1
                count1, count2 = 1, 0
        return res

            