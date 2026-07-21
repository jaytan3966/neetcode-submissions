class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        starStack = []
        n = len(s)

        for i in range(n):
            if s[i] == '(':
                leftStack.append('(')
            elif s[i] == ')':
                if not leftStack and not starStack: return False

                if leftStack: leftStack.pop()
                else: starStack.pop()
            else:
                starStack.append('*')
        return len(leftStack)<=len(starStack)
