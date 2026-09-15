class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}

        for i in range(len(t)):
            target[t[i]] = target.get(t[i], 0)+1

        l = 0
        n = len(s)
        cur = {}
        found = len(target)
        found_chars = set()

        ans = ""
        shortest_len = float('inf')
        for r in range(n):
            if s[r] in target:
                cur[s[r]] = cur.get(s[r], 0)+1

                if cur[s[r]] >= target[s[r]] and s[r] not in found_chars:
                    found_chars.add(s[r])
                    found-=1

            while found == 0:
                if (r-l+1)<shortest_len:
                    shortest_len = r-l+1
                    ans = s[l:r+1]
                if s[l] in target:
                    cur[s[l]]-=1

                    if cur[s[l]]<target[s[l]]: 
                        found+=1
                        found_chars.remove(s[l])
                l+=1
        return ans
