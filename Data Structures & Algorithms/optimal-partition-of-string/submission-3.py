class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        pieces = 1
        n = len(s)

        for i in range(n):
            char = s[i]

            if char in seen:
                seen.clear()
                pieces+=1
            
            seen.add(char)
        return pieces
