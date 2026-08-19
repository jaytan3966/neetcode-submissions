class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        seen = set()
        ans = 0

        for r in range(n):
            while seen and s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            ans = max(ans, r-l+1)
        return ans