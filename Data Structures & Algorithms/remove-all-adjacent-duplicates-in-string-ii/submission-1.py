class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stack = []

        for i in range(n):
            if stack and stack[-1][0] == s[i]:
                stack[-1][1]+=1
            else:
                stack.append([s[i], 1])
            while stack and stack[-1][1]==k:
                stack.pop()

        ans = ''
        for char, cnt in stack:
            ans+=(char*cnt)
        return ans
            

        