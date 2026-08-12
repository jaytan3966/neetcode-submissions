class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n, m = len(s), len(dictionary)
        dic = set(dictionary)

        lens = []

        for i in range(m):
            lens.append(len(dictionary[i]))

        l = 0
        ans = 0
        k = len(lens)
        while l<n:
            og = l
            for i in range(k):
                if l+lens[i]<n and s[l:l+lens[i]] in dic:
                    l+=lens[i]
                    break
            if l == og: 
                l+=1
                ans+=1
        return ans