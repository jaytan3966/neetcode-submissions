class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        n = len(hand)

        for i in range(n):
            cur = hand[i]

            while counts[cur-1]>0:
                cur-=1

            if counts[cur]>0:
                for i in range(groupSize):
                    if cur+i not in counts or counts[cur+i]==0:
                        return False
                    counts[cur+i]-=1

        return True