class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]: return ""
        ans = ""
        for word in strs:
            ans+=word+" "
        return ans
    def decode(self, s: str) -> List[str]:
        if s == "": return [""]
        lst = s.split()
        return lst