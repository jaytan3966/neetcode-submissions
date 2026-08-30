class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        affected = 0
        n = len(hand)

        for i in range(n):
            cur = hand[i]

            if cur-1 in counts and counts[cur-1]>0: continue

            if counts[cur]>0:
                for i in range(groupSize):
                    if cur+i not in counts or counts[cur+i]==0:
                        return False
                    counts[cur+i]-=1
                    affected+=1
        return affected == n