class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        values = []

        ans = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(values.pop(0))
            values.append(s[i])
            seen.add(s[i])
            ans = max(ans, len(values))
        return ans