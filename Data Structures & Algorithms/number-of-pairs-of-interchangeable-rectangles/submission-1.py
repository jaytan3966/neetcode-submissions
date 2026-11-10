class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_pairs = {}
        ans = 0
        for w, h in rectangles:
            ratio = w/h

            ratio_pairs[ratio] = ratio_pairs.get(ratio, 0)+1
        
        for ratio in ratio_pairs:
            ans+=((ratio_pairs[ratio]*(ratio_pairs[ratio]-1))//2)

        return ans
