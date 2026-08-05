class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        inR = deque([])
        outR = deque([])

        inD = deque([])
        outD = deque([])

        n = len(senate)

        for i in range(n):
            ch = senate[i]

            if ch == 'R':
                if inD:
                    outR.append(ch)
                    outD.append(inD.popleft())
                else:
                    inR.append(ch)
                    if outD: outD.popleft()
            else:
                if inR:
                    outD.append(ch)
                    outR.append(inR.popleft())
                else:
                    inD.append(ch)
                    if outR: outR.popleft()
        return "Radiant" if outR else "Dire"
