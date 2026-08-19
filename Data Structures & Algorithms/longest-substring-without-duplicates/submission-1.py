class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 1
        ans = 1
        seen = set(s[0])
        while j<len(s):
            while s[j] in seen and i<j:
                seen.remove(s[i])
                ans = max(ans, j-i)
                i+=1
            ans = max(ans, j-i+1)
            seen.add(s[j])
            j+=1

        return ans