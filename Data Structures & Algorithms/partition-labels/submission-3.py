class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_inds = {}
        n = len(s)

        for i in range(n):
            last_inds[s[i]] = i
        
        ans = []
        size = end = 0
        for r in range(n):
            size+=1
            end = max(last_inds[s[r]], end)

            if r == end:
                ans.append(size)
                size = 0
        return ans

