class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans+=str(len(word))+word
        return ans
    def decode(self, s: str) -> List[str]:
        l = 0
        ans = []
        n = len(s)
        print(s)
        while l<n:
            cnt = ""
            while l<n and s[l].isdigit():
                cnt+=s[l]
                l+=1

            cnt = int(cnt)
            wind = l+cnt
            word = ""

            while l<wind:
                word+=s[l]
                l+=1
            ans.append(word)
        return ans