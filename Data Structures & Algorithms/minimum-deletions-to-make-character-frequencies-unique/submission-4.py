class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(s)

        used = set()
        
        ans = 0
        for char in counts:
            count = counts[char]
            while count in used:
                count-=1
                ans+=1
                if count == 0:
                    break
            used.add(count)
        return ans
