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
                if openings:
                    openings.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        while openings:
            if not stars: return False
            if openings[-1]>stars[-1]: return False
            stars.pop()
            openings.pop()
        return True