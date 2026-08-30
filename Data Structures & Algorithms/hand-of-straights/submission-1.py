class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        
        hand.sort()
        n = len(hand)

        for i in range(n):
            cur = hand[i]

            if counts[cur]>0:
                for i in range(groupSize):
                    if cur+i not in counts or counts[cur+i]==0:
                        return False
                    counts[cur+i]-=1
        return True