class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans+=word+" "
        print(ans)
        return ans
    def decode(self, s: str) -> List[str]:
        lst = s.split()
        return lst