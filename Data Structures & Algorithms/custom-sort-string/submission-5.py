class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)

        ans = ""

        n = len(order)
        for i in range(n):
            if order[i] in counts:
                ans+=(order[i]*counts[order[i]])
                del counts[order[i]]
        
        for char in counts:
            ans+=(char*counts[char])
        
        return ans