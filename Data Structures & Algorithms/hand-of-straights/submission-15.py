class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)

        for num in hand:
            if not counts[num]: continue
            
            start = num

            while counts[start-1]: start-=1

            for cur in range(start, start+groupSize):
                if counts[cur]==0: return False
                counts[cur]-=1
        return True

        