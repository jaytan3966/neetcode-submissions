class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        ans = ""
        for word in strs:
            ans+=word+" "
        return ans
    def decode(self, s: str) -> List[str]:
        if len(s) == 1: return [s]
        lst = s.split()
        return lst