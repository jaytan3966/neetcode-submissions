class Solution:
    def partitionString(self, s: str) -> int:
        original_counts = Counter(s)
        counts = Counter(s)
        pieces = 1
        n = len(s)

        for i in range(n):
            char = s[i]

            if original_counts[char]-counts[char] == 1:
                original_counts = dict(counts)
                pieces+=1
            
            counts[char]-=1
        return pieces
