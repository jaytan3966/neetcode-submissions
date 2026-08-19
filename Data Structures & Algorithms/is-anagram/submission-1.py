class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) != set(t):
            return False

        from collections import Counter

        first = Counter(s)
        sec = Counter(t)
        x = set(s)
        y = set(t)

        for char in x:
            if first[char] != sec[char]:
                return False
        return True
