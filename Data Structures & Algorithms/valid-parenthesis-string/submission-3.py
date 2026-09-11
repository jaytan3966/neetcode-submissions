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
        return len(stars)>=len(openings)