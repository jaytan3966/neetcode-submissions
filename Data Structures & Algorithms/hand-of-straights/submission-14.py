class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        counts = Counter(hand)

        for num in hand:
            if counts[num]==0: continue

            for cur in range(num, num+groupSize):
                if counts[cur]==0: return False
                counts[cur]-=1
        return True

        