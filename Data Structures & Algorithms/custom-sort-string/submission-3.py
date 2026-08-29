class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        n = len(order)
        ans = ''

        for l in range(n):
            if counts.get(order[l],0)>0:
                ans+=(order[l]*counts[order[l]])
                counts[order[l]] = 0
        for c in counts:
            count = counts[c]
            ans+=(c*count)
            counts[c] = 0
        return ans