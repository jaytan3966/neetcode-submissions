class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        ans = 0
        if len(s) == 0:
            return 0

        seen = set(s[0])
        for j in range(1, len(s)):
            while s[j] in seen and i<j:
                seen.remove(s[i])
                i+=1
            ans = max(ans, j-i+1)
            seen.add(s[j])

        return ans