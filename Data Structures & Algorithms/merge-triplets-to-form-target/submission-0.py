class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found1 = False
        found2 = False
        found3 = False
        for x,y,z in triplets:
            if x>target[0] or y>target[1] or z>target[2]:
                continue
            if x == target[0]: found1 = True
            if y == target[1]: found2 = True
            if z == target[2]: found3 = True
        return found1 and found2 and found3
            
