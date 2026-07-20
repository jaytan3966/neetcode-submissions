class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = [0]*26

        for char in s1:
            target[ord(char)-ord('a')]+=1
        
        guess = [0]*26

        for i in range(len(s1)):
            guess[ord(s2[i])-ord('a')]+=1
        
        i, j = 0, len(s1)-1
        while j < len(s2):
            if guess == target:
                return True
            guess[ord(s2[i])-ord('a')]-=1
            i+=1
            j+=1
            if j<len(s2):
                guess[ord(s2[j])-ord('a')]+=1
        return False