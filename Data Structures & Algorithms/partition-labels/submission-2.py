class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_inds = {}
        n = len(s)

        for i in range(n):
            last_inds[s[i]] = i
        
        ans = []
        l = 0
        cur_last = -1
        for r in range(n):
            if cur_last == -1:
                cur_last = last_inds[s[r]]
                l = r

                if cur_last == r:
                    ans.append(cur_last-l+1)
                    cur_last = -1
            else:
                if r == cur_last:
                    ans.append(cur_last-l+1)
                    cur_last = -1
                else:
                    if last_inds[s[r]]>cur_last:
                        cur_last = last_inds[s[r]]
        return ans

