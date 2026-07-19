class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = [0] * 26

        for i in range(len(s1)):
            letters[ord(s1[i])-ord("a")]+=1

        copy = letters[:]
        permutating = False

        for i in range(len(s2)):
            if letters[ord(s2[i])-ord("a")] != 0 and not permutating:
                permutating = True
                letters[ord(s2[i])-ord("a")]-=1
            
            elif permutating:
                if letters[ord(s2[i])-ord("a")] == 0:
                    permutating = False
                    letters = copy
                else: letters[ord(s2[i])-ord("a")]-=1

            if letters == [0] * 26: return True
        return False