class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        ans = 0

        l = 0
        count[s[l]]+=1
        maxFreq = 1
        for r in range(1, len(s)):
            count[s[r]]+=1
            maxFreq = max(maxFreq, count[s[r]])

            while (r-l+1)-maxFreq > k:
                count[s[l]]-=1
                l+=1
            ans = max(ans, r-l+1)
        return ans

        