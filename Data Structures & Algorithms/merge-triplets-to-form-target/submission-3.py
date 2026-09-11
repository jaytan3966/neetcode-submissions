class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        foundA, foundB, foundC = False, False, False

        for x,y,z in triplets:

            if x>target[0] or y>target[1] or z>target[2]: continue
            
            if x==target[0]:
                foundA = True
            if y==target[1]:
                foundB = True
            if z==target[2]:
                foundC = True

            if foundA and foundB and foundC: return True
            
        return False