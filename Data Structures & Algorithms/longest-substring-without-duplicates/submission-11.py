class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        if s == "": return ans

        seen = set()
        l = 0
        seen.add(s[l])

        for r in range(1, len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            ans = max(ans, r-l+1)
            seen.add(s[r])
        return ans
            