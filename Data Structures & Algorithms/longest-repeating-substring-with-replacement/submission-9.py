class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        freqs = {}
        maxF = 0

        for j in range(len(s)):
            freqs[s[j]] = freqs.get(s[j], 0)+1
            maxF = max(maxF, freqs[s[j]])

            while (j-i+1) - maxF > k:
                i+=1
        return j-i+1


