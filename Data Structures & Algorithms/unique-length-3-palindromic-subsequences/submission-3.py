class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        ans = 0

        lets = set(s)
        seen = set()

        for i in range(n):
            for let in lets:
                if let+s[i]+let in seen: continue
                first, last = s.find(let), s.rfind(let)
                if first<i<last:
                    ans+=1
                    print(i,let+s[i]+let)
                    seen.add(let+s[i]+let)
        return ans