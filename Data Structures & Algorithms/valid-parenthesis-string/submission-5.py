class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        stars = []
        openings = []

        for i in range(n):
            if s[i] == '(':
                openings.append(i)
            elif s[i] == '*':
                stars.append(i)
            else:
                if openings and openings[-1]<i:
                    openings.pop()
                elif stars and stars[-1]<i:
                    stars.pop()
                else:
                    return False
        
        m = len(openings)

        if m>0:
            for i in range(m-1, -1, -1):
                if stars and stars[-1]>openings[i]:
                    openings.pop()
                    stars.pop()
        return len(openings)==0