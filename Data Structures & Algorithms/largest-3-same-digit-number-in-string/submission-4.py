class Solution:
    def largestGoodInteger(self, num: str) -> str:

        ans = ""
        greatest = float('-inf')
        l = 0
        n = len(num)

        for i in range(n-2):
            if num[i]==num[i+1]==num[i+2]:
                nm = num[i:i+3]
                if int(nm)>greatest:
                    greatest = int(nm)
                    ans = nm
            print(i)

        if greatest == float('-inf'): return ""

        return ans
